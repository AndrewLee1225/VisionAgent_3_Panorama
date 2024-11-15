# Panorama Video Maker_ver.1

## Project Overview
Panorama Video Maker is a Python application that allows users to collect video frames, create panoramas from multiple images, and save the resulting stitched panorama. The application utilizes OpenCV for image processing and PyQt5 for the graphical user interface (GUI).

## Features
- **Collect Video Frames**: Capture frames from a live video stream using your webcam.
- **View Collected Frames**: View the collected frames in a single stacked display.
- **Stitch Images**: Stitch the collected frames into a panorama using OpenCV's stitching functionality.
- **Save Panorama**: Save the stitched panorama as an image file.
- **User-Friendly GUI**: Intuitive interface to manage video collection, stitching, and saving operations.

## Installation
To use Panorama Video Maker, you need to set up a Python environment with the required dependencies. You can use the `pyproject.toml` or `requirements.txt` to manage dependencies.

### Prerequisites
- Python 3.8 or higher
- `opencv-python` for image processing
- `PyQt5` for the graphical user interface
- `numpy` for array manipulations

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd panorama-video-maker
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, use `pyproject.toml` to install dependencies with Poetry:
   ```bash
   poetry install
   ```

## Usage
1. Run the main script to start the application:
   ```bash
   python cva3.py
   ```
2. Use the GUI to:
   - Click "Collect Video" to start capturing video frames.
   - Press 'c' to capture a frame or 'q' to stop capturing.
   - Click "Show Images" to view collected frames.
   - Click "Stitch Images" to create a panorama.
   - Click "Save Panorama" to save the stitched result.
   - Click "Quit" to close the application.

## Creating an Executable
You can create a standalone executable of the application using `pyinstaller`:
1. Install `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Create an executable:
   ```bash
   pyinstaller --onefile main.py
   ```
   The executable will be available in the `dist` directory.

## Project Structure
```
panorama-video-maker/
├── main.py              # Main application script
├── README.md            # Project documentation
├── pyproject.toml       # Project dependencies and metadata
├── requirements.txt     # List of dependencies
└── dist/                # Directory for the executable (generated by pyinstaller)
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- **OpenCV** for the image processing capabilities.
- **PyQt5** for providing the GUI framework.

# Panorama Video Maker_ver.2

## Overview
The **Panorama Video Maker** is a Python-based GUI application that allows users to capture video frames from a webcam and create a panorama image by stitching those frames together. The application uses the PyQt5 framework for the user interface and OpenCV for image processing.

This updated version includes several improvements to enhance user experience and image stitching quality.

## Features
- **Video Collection**: Collect multiple frames from a webcam to create a panorama.
- **Show Images**: View the collected frames before stitching.
- **Image Stitching**: Stitch collected frames into a seamless panorama image with enhanced preprocessing.
- **Save Panorama**: Save the resulting stitched panorama image to your local storage.
- **Quit Application**: Exit the application safely.

## Improvements in the Updated Version
1. **Enhanced Stitching Quality**:
   - Added Gaussian blur preprocessing to frames before stitching. This improves the alignment and blending of overlapping regions, resulting in a more natural panorama.

2. **Better User Feedback**:
   - During frame collection, the application now displays the number of frames collected, providing real-time feedback.
   - Updated messages to better inform users about the progress of stitching and the status of operations.

3. **Improved Image Display**:
   - Images are displayed sequentially during the "Show Images" function, with each image shown for 500 milliseconds for better visualization.

## Requirements
- **Python 3.6+**
- **PyQt5**: To install PyQt5, run `pip install PyQt5`
- **OpenCV**: To install OpenCV, run `pip install opencv-python`

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```sh
   cd panorama-video-maker
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## How to Use
1. **Run the Application**:
   ```sh
   python cva3.py
   ```
2. **Collect Video Frames**:
   - Click **Collect Video** to start capturing frames from your webcam.
   - Press **'c'** to capture frames and **'q'** to stop the collection.
3. **Show Images**:
   - Click **Show Images** to preview the collected frames.
4. **Stitch Images**:
   - Click **Stitch Images** to stitch the frames into a panorama.
   - The progress bar will indicate stitching progress, and you will see a message when stitching is successful.
5. **Save Panorama**:
   - Click **Save Panorama** to save the resulting panorama image.
6. **Quit**:
   - Click **Quit** to exit the application.

## Notes
- Ensure good lighting and minimal movement in the scene while capturing frames for best results.
- The application requires at least **two frames** to proceed with stitching.

## Troubleshooting
- **Camera Not Opening**: Make sure that your webcam is not being used by another application.
- **Stitching Failed**: If the panorama stitching fails, try capturing frames with more overlap and less movement between them. The Gaussian blur preprocessing helps improve results but may not fix all issues.
- **Missing Dependencies**: Ensure all dependencies are installed using the command `pip install -r requirements.txt`.

## Future Improvements
- **Automatic Frame Capture**: Add an option for automatic frame capture at set intervals to streamline the collection process.
- **Advanced Blending Techniques**: Implement more advanced blending techniques to improve the quality of the stitched panorama.
- **Support for Image Import**: Allow users to import pre-captured images from local storage instead of capturing directly from the webcam.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments
- **PyQt5** for the GUI components.
- **OpenCV** for providing powerful image processing capabilities.

## Contact
For any inquiries or issues, please contact [lyandrew1225@gmail.com].

# Panorama Video Maker_ver.3

## Overview
Panorama Video Maker is a GUI application built with PyQt5 and OpenCV to create panorama images by stitching frames collected from a video feed. The application allows users to:

- Collect video frames automatically using a webcam.
- Show the collected frames.
- Stitch the collected frames into a panoramic image.
- Save the stitched panoramic image to a file.

This README will guide you through the installation process, how to use the application, and the improvements made to the original code.

## Features
1. **Automatic Frame Collection**: Collect frames automatically at 2-second intervals from the webcam, making it easier for users to gather the required images without manually interacting every time.
2. **User-Friendly GUI**: Provides a simple interface for collecting frames, displaying images, stitching them, and saving the panorama.
3. **Multi-Threaded Processing**: Uses multi-threading to ensure the GUI remains responsive during long-running operations such as frame collection and image stitching.
4. **Progress Indication**: Shows a progress bar to indicate the stitching process's completion.

## Improvements Made
1. **Automated Frame Collection**: Previously, users needed to manually capture frames by pressing a button each time. Now, frames are automatically collected every 2 seconds, improving efficiency and user experience.
2. **Multi-Threading**: Frame collection and stitching processes are executed in separate threads to ensure that the application remains responsive while performing these potentially time-consuming tasks.
3. **Enhanced Error Handling**: Added descriptive messages to guide the user if something goes wrong (e.g., camera not available or not enough frames collected).
4. **Stitching Feedback**: Improved user feedback by updating the progress bar and adding more detailed status messages during the stitching process.

## Installation

To run Panorama Video Maker, follow these steps:

### Prerequisites
- Python 3.6 or higher
- Required Python packages:
  - PyQt5
  - OpenCV (cv2)
  - numpy

You can install the required packages using pip:

```bash
pip install PyQt5 opencv-python numpy
```

### Running the Application

1. Clone this repository or download the Python script.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

```bash
python cva3.py
```

## Usage Instructions

1. **Launch the Application**: Run the script to open the GUI.
2. **Collect Frames**: Click the "Collect Video" button to start collecting frames from the webcam. The frames will be automatically captured every 2 seconds. Press 'q' to stop the collection.
3. **Show Collected Frames**: Click "Show Images" to view the frames that were collected.
4. **Stitch Images**: Click "Stitch Images" to create a panorama from the collected frames. This process may take some time, and progress will be shown in the progress bar.
5. **Save Panorama**: Once the panorama is successfully created, click "Save Panorama" to save the stitched image to your local storage.
6. **Quit Application**: Click the "Quit" button to exit the application.

## GUI Elements
- **Collect Video**: Starts the frame collection process from the webcam.
- **Show Images**: Displays the frames collected so far.
- **Stitch Images**: Stitches the collected frames into a panorama.
- **Save Panorama**: Saves the stitched panorama image.
- **Quit**: Closes the application.
- **Label**: Displays the current status or instructions for the user.
- **Progress Bar**: Shows the progress of the stitching process.

## Known Issues
- **Stitching Failure**: In some cases, stitching may fail if the frames do not have enough overlap or features for proper alignment. The user will be notified if stitching fails, and they may need to collect new frames.
- **Webcam Access**: The application uses the default webcam. Ensure no other applications are using the webcam, or the application might fail to access it.

## Future Improvements
- **Support for External Cameras**: Add the ability to choose between multiple camera sources.
- **Manual Frame Selection**: Allow users to manually select frames from the collected set to improve stitching accuracy.
- **Improved Stitching Algorithm**: Provide options to use different stitching algorithms or fine-tune parameters for better results.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
- **OpenCV**: For providing powerful image processing and computer vision tools.
- **PyQt5**: For the GUI framework that made building this application straightforward.
