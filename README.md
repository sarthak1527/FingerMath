# FingerMath

FingerMath is a real-time computer vision application built using Python, OpenCV, and MediaPipe. The application detects hand landmarks from a webcam feed and counts fingertips placed inside predefined target boxes.

This project demonstrates real-time hand tracking and landmark detection, making it suitable for educational demonstrations, computer vision learning, and interactive applications.

## Features

- Real-time webcam-based hand tracking
- Detection of up to two hands
- Fingertip detection using MediaPipe
- Counts fingertips inside customizable target boxes
- Displays individual box counts and total count
- Built using OpenCV for real-time image processing

## Technologies Used

- Python
- OpenCV
- MediaPipe Tasks API
- NumPy

## Project Structure

```text
FingerMath/
│── main.py
│── hand_landmarker.task
│── requirements.txt
│── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/FingerMath.git
cd FingerMath
```

Create a virtual environment:

```bash
python -m venv cv_env
```

Activate the virtual environment.

macOS/Linux:

```bash
source cv_env/bin/activate
```

Windows:

```bash
cv_env\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Download the `hand_landmarker.task` model from the official MediaPipe Models repository and place it in the project directory or use it from the repo.

## Running the Project

```bash
python main.py
```

## How It Works

1. Captures live video from the webcam.
2. Detects hand landmarks using MediaPipe.
3. Tracks the five fingertips of each detected hand.
4. Checks whether each fingertip lies inside either target box.
5. Displays the count for each box along with the total number of fingertips detected.

## Future Improvements

- Dynamic target boxes
- Gesture recognition
- Pose-based game modes
- Timer and scoring system
- Sound effects and animations
- Multiplayer support
- Difficulty levels

## Applications

- Computer Vision
- Human-Computer Interaction
- Gesture Recognition
- Educational Demonstrations
- Interactive Learning

## Author

**Sarthak Acharya**

Bachelor of Electronics, Communication and Information Engineering
