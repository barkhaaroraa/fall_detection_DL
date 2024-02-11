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

### Working of the Prototype
[Working Demo with Fall Detection and Face Recognition](https://drive.google.com/file/d/1HhNCq11J1ZNmuDoxo6KYVFS1S7IJZid7/view?usp=sharing)

## How it works

### Video Capture: 
The system captures live video using OpenCV, allowing it to monitor individuals in real-time.

### Landmark Detection: 
MediaPipe library is used to detect landmarks on the human body, such as shoulders, elbows, and hips. These landmarks help in tracking the movements of individuals in the video.

### Fall Detection Algorithm: 
The system periodically checks the previous coordinates of the shoulders of the person in the frame, typically every 4 seconds. If there is a significant drop in the height of the shoulders, it indicates a potential fall.

### Face Detection:
Facial recognition using the facial_recognition library helps identify individuals in the video. This information is then used to retrieve contextual data from the integrated database about the person who has fallen.

### Alert Triggering:
When a fall is detected, the system prints "Fall Detected" and retrieves relevant information about the individual from the database. This information includes medical history, emergency contact details, and specific care instructions.

### Integration with Healthcare Authorities and Guardians:
The database contains comprehensive information about the individuals being monitored, securely storing their medical history and emergency contact details. Healthcare authorities and guardians receive immediate notifications via Telegram with detailed information about the incident, enabling them to initiate a timely response. Healthcare authorities coordinate assistance efforts based on the information provided, dispatching appropriate medical personnel or emergency responders to the location.

