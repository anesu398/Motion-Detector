# Webcam Motion Detector

This project is a Python-based motion detection system that captures video from a webcam and detects motion in real-time. It uses OpenCV library for computer vision tasks and provides a simple interface to visualize detected motion.

## Features

- **Real-time Motion Detection**: Captures video from a webcam and detects motion in real-time.
- **Motion Highlighting**: Highlights moving objects within the webcam stream with bounding boxes.
- **Adjustable Parameters**: Parameters like threshold value and contour area threshold are adjustable to fine-tune motion detection sensitivity.
- **Simple Interface**: Provides a straightforward interface for displaying the webcam stream with motion detection overlays.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/webcam-motion-detector.git
    ```

2. Navigate to the project directory:

    ```bash
    cd webcam-motion-detector
    ```

3. Install dependencies:

    ```bash
    pip install opencv-python numpy
    ```

## Usage

1. Run the script:

    ```bash
    python motion_detector.py
    ```

2. Adjust parameters (optional):

    - Modify threshold value and contour area threshold in the script to fine-tune motion detection sensitivity.

3. View webcam stream with motion detection overlays.

4. Press 'q' to exit the application.

## Parameters

- **Threshold Value**: Adjust the threshold value to control the sensitivity of motion detection.
- **Contour Area Threshold**: Adjust the contour area threshold to filter out small movements.

## Example

Here's a sample output of the motion detector:

![Motion Detector Example](example.png)

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
