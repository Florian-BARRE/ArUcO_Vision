# ArUcO_Vision
This project is designed to enhance real-time image processing applications by providing a reliable means of detecting and localizing Aruco codes. Through meticulous camera calibration and sophisticated image analysis, it achieves high accuracy in positioning Aruco markers, even in complex environments.
# Aruco Code Detection and Localization Project

Aruco Code Detection and Localization is a sophisticated image processing project aimed at detecting Aruco markers in images and precisely determining their coordinates (x, y) relative to the camera's position. This project incorporates advanced camera calibration, video stream compression, and computational methods to accurately identify and locate Aruco codes, making it ideal for augmented reality applications and spatial positioning tasks.

## Project Overview
This project is designed to enhance real-time image processing applications by providing a reliable means of detecting and localizing Aruco codes. Through meticulous camera calibration and sophisticated image analysis, it achieves high accuracy in positioning Aruco markers, even in complex environments.

### Key Features
- **Camera Calibration**: Utilizes `calibrate_camera.py` and a set of `calibration_images` to correct for lens distortion, ensuring precise detection and localization of Aruco codes.
- **Aruco Code Detection**: The main functionality, implemented in `main.py`, processes images to detect Aruco markers and calculates their positions in real-time.
- **Precise Localization**: Advanced computational methods deduce the 2D coordinates of detected Aruco codes, offering accurate spatial information.
- **Video Stream Compression**: Includes tools for compressing video streams, optimizing performance for real-time applications.
- **Flexible Configuration**: `configuration.py` allows for easy adjustments to detection parameters and calibration settings, tailoring the system to various operational requirements.
- **Comprehensive Dependency Management**: A `requirements.txt` file ensures all necessary Python packages are installed, facilitating a smooth setup process.

### How It Works
- **Initialization**: Begins with camera calibration to optimize accuracy in Aruco detection.
- **Detection and Localization**: Continuously scans for Aruco markers in the camera's field of view, applying calibration corrections to precisely calculate their coordinates.
- **Real-Time Processing**: Compresses video streams and employs efficient algorithms to maintain performance in real-time applications.

### Getting Started
1. **Prerequisites**: Ensure Python 3.x is installed. Familiarity with virtual environments is recommended.
2. **Installation**: Clone the repository, set up a virtual environment, activate it, and install dependencies from `requirements.txt`.
3. **Calibration**: Use `calibrate_camera.py` with the provided calibration images to generate distortion correction coefficients.
4. **Running the Detection**: Execute `main.py` to start the detection process, displaying Aruco codes' positions in real-time.

### Configuration
Customize `configuration.py` to adjust detection sensitivity and other settings, optimizing the system for your specific use case.

### Contributing
Contributions are welcome to enhance detection algorithms, expand features, or improve efficiency. Please submit pull requests or open issues for discussion.

### License
Specify the project's license, outlining how others may use or contribute to the code.

## Conclusion
The Aruco Code Detection and Localization project is a cutting-edge solution for applications requiring precise spatial positioning. Its robust architecture and advanced features make it an invaluable tool for augmented reality, spatial analysis, and beyond.
