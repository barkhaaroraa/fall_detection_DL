# Fall Detection using OpenCV and MediaPipe
This project is aimed at developing a fall detection system using OpenCV and MediaPipe libraries in Python. The system detects falls by monitoring the movements of individuals captured in live video feeds and triggers an alert when a fall is detected. The implementation involves capturing the video using OpenCV, marking landmarks using MediaPipe, and analyzing the movements to identify falls.

## Requirements
To run this project, you need to have the following libraries installed:

OpenCV (import cv2)
MediaPipe (import mediapipe as mp)
Python (from time import time)
You can install the required libraries using pip:

Copy code
` pip install opencv-python
pip install mediapipe ` 

## How it works

### Video Capture: 
The system captures live video using OpenCV, allowing it to monitor individuals in real-time.

### Landmark Detection: 
MediaPipe library is used to detect landmarks on the human body, such as shoulders, elbows, and hips. These landmarks help in tracking the movements of individuals in the video.

### Fall Detection Algorithm: 
The system periodically checks the previous coordinates of the shoulders of the person in the frame, typically every 4 seconds. If there is a significant drop in the height of the shoulders, it indicates a potential fall.

### Alert Triggering: 
When a fall is detected, the system prints "Fall Detected". Further improvements could involve integrating the system with emergency helplines or healthcare agencies to provide immediate assistance, especially for elderly individuals or patients with medical vulnerabilities.
