# Python Vision

`Python Vision` is a Python program that allows you to control your mouse using hand gestures. It leverages OpenCV and MediaPipe for hand tracking and gesture recognition.

## Features

- **Hand Detection and Tracking**: Uses MediaPipe to detect and track hand landmarks.
- **Mouse Control**: Move the mouse cursor with your index finger.
- **Click Detection**: Perform left-click actions by pressing your thumb on the PIP joint of your index finger.
- **Focus Mouse**: Keeping your middle finger up allow you to focus your mouse at a point (stop the flickering) and click easily.

## Requirements

- Python 3.6+

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dr4g0n369/pythonVision.git
    cd pythonVision
    ```

2. Create a virtual environment
    ```bash
    python -m venv env
    ```

2. Install the required packages:
    ```bash
    source ./env/Scripts/activate
    pip install -r requirements.txt
    ```

## Usage

1. Run the program:
    ```bash
    python handMouseControl.py 
    ```
    Make sure you are running it from the virtual environment created.

2. A window will open showing the webcam feed. Move your index finger to control the mouse cursor.

## Code Overview

- `handDetector`: A class for detecting and tracking hands using MediaPipe.
- `handMouseControl.py`: The main script to run the hand gesture-based mouse control.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [pynput](https://pynput.readthedocs.io/)
- Inspired by [this video tutorial](https://www.youtube.com/watch?v=01sAkU_NvOY).
