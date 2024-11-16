import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QProgressBar
import cv2 as cv
import numpy as np
import sys
import winsound
import threading
import time

class Panorama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the base directory
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Set the window properties
        self.setWindowTitle("Panorama Video Maker")
        self.setGeometry(200, 200, 700, 300)

        # Create buttons, labels, and progress bar
        self.collectButton = QPushButton("Collect Video", self)
        self.showButton = QPushButton("Show Images", self)
        self.stitchButton = QPushButton("Stitch Images", self)
        self.saveButton = QPushButton("Save Panorama", self)
        self.quitButton = QPushButton("Quit", self)
        self.label = QLabel("Welcome!", self)
        self.progressBar = QProgressBar(self)

        # Set button positions and properties
        self.collectButton.setGeometry(10, 25, 100, 30)
        self.showButton.setGeometry(120, 25, 100, 30)
        self.stitchButton.setGeometry(230, 25, 100, 30)
        self.saveButton.setGeometry(340, 25, 100, 30)
        self.quitButton.setGeometry(450, 25, 100, 30)
        self.label.setGeometry(10, 70, 600, 50)
        self.progressBar.setGeometry(10, 130, 600, 30)

        # Initially disable some buttons
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)

        # Connect buttons to their respective functions
        self.collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)
        self.stitchButton.clicked.connect(self.stitchFunction)
        self.saveButton.clicked.connect(self.saveFunction)
        self.quitButton.clicked.connect(self.quitFunction)

    def collectFunction(self):
        # Disable buttons during video collection
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.label.setText("Collecting frames automatically. Press 'q' to stop.")

        # Open the default camera
        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not self.cap.isOpened():
            sys.exit("Failed to open camera")

        # List to store collected frames
        self.imgs = []
        # Start a new thread to collect frames from the camera
        threading.Thread(target=self.collectFrames).start()

    def collectFrames(self):
        start_time = time.time()
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Display the current frame in a window
            cv.imshow('Video Display', frame)
            current_time = time.time()

            # Automatically collect frames every 2 seconds
            if current_time - start_time >= 2:
                self.imgs.append(frame.copy())  # Save a copy of the current frame
                self.label.setText(f"Collected {len(self.imgs)} frames")  # Update the label with the number of collected frames
                start_time = current_time

            # Stop collecting frames when 'q' is pressed
            key = cv.waitKey(1)
            if key == ord('q'):
                self.cap.release()
                cv.destroyWindow('Video Display')
                break

        # Enable buttons if at least two frames are collected
        if len(self.imgs) >= 2:
            self.showButton.setEnabled(True)
            self.stitchButton.setEnabled(True)
            self.label.setText("Video collection complete. Ready to proceed.")
        else:
            self.label.setText("Not enough frames collected. Please collect at least 2 frames.")

    def showFunction(self):
        # Check if there are images to show
        if not self.imgs:
            self.label.setText("No images to show.")
            return

        self.label.setText(f"Number of images collected: {len(self.imgs)}")
        # Display each collected image one by one
        for img in self.imgs:
            resized_img = cv.resize(img, dsize=(0, 0), fx=0.25, fy=0.25)  # Resize image to 25% of original size
            cv.imshow('Image Collection', resized_img)
            cv.waitKey(500)  # Show each image for 500 ms
        cv.destroyAllWindows()

    def stitchFunction(self):
        # Reset progress bar and update label
        self.progressBar.setValue(0)
        self.label.setText("Stitching images, please wait...")

        # Run stitching in a separate thread to keep UI responsive
        threading.Thread(target=self.stitchImages).start()

    def stitchImages(self):
        # Create a stitcher object
        stitcher = cv.Stitcher_create()
        
        # Preprocess images for better stitching (apply Gaussian blur)
        preprocessed_imgs = [cv.GaussianBlur(img, (5, 5), 0) for img in self.imgs]

        # Perform stitching on the preprocessed images
        status, stitched_img = stitcher.stitch(preprocessed_imgs)

        # Check if stitching was successful
        if status == cv.Stitcher_OK:
            self.img_stitched = stitched_img
            # Display the stitched panorama
            cv.imshow('Stitched Panorama', self.img_stitched)
            self.label.setText("Panorama stitching successful!")
            self.progressBar.setValue(100)  # Update progress bar to 100%
            self.saveButton.setEnabled(True)  # Enable the save button
        else:
            # Play a beep sound to indicate failure and update label
            winsound.Beep(3000, 500)
            self.label.setText("Panorama stitching failed. Please try again with different frames.")
            self.progressBar.setValue(0)

    def saveFunction(self):
        # Check if there is a stitched image to save
        if not hasattr(self, 'img_stitched'):
            self.label.setText("No panorama to save.")
            return

        # Open a file dialog to choose where to save the panorama
        fname, _ = QFileDialog.getSaveFileName(self, "Save File", os.path.join(self.BASE_DIR, "panorama.jpg"), "Images (*.png *.xpm *.jpg)")
        if fname:
            # Save the stitched image to the selected file
            cv.imwrite(fname, self.img_stitched)
            self.label.setText(f"Panorama saved to {fname}")

    def quitFunction(self):
        # Release the camera if it is still open
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        # Close all OpenCV windows and the application
        cv.destroyAllWindows()
        self.close()

if __name__ == "__main__":
    # Create the application and main window
    app = QApplication(sys.argv)
    win = Panorama()
    win.show()
    # Execute the application
    sys.exit(app.exec_())