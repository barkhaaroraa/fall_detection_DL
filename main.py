import facial_recognition as fr

import os
import cv2
import numpy as np
import math
import mediapipe as mp
from time import time

previous_avg_shoulder_height = 0

def detectPose(frame, pose_model, display=True):
    modified_frame = frame.copy()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose_model.process(frame_rgb)
    height, width, _ = frame.shape
    landmarks = []
    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            landmarks.append((int(landmark.x * width), int(landmark.y * height),
                              (landmark.z * width)))
        connections = mp.solutions.pose.POSE_CONNECTIONS
        for connection in connections:
            start_point = connection[0]
            end_point = connection[1]
            cv2.line(modified_frame, (landmarks[start_point][0], landmarks[start_point][1]),
                     (landmarks[end_point][0], landmarks[end_point][1]), (0, 255, 0), 3)
    else:
        return None, None  
    if display:
        cv2.imshow('Pose Landmarks', modified_frame)
    return modified_frame, landmarks

def detectFall(landmarks, height, previous_avg_shoulder_height):

    left_shoulder_y = landmarks[11][1]
    right_shoulder_y = landmarks[12][1]
    
    # Calculate the average y-coordinate of the shoulder
    avg_shoulder_y = (left_shoulder_y + right_shoulder_y) / 2

    if(previous_avg_shoulder_height==0):
        previous_avg_shoulder_height=avg_shoulder_y
        return False,previous_avg_shoulder_height
    fall_threshold = previous_avg_shoulder_height * 1.5
    print(previous_avg_shoulder_height, avg_shoulder_y,end="\n")
    
    # Check if the average shoulder y-coordinate falls less than the previous average shoulder height
    if avg_shoulder_y > fall_threshold:
        previous_avg_shoulder_height = avg_shoulder_y
        return True, previous_avg_shoulder_height
    else:
        previous_avg_shoulder_height = avg_shoulder_y
        return False, previous_avg_shoulder_height


frr = fr.FaceRecognition()
frr.encode_faces()
pose_video = mp.solutions.pose.Pose(static_image_mode=False, min_detection_confidence=0.7, model_complexity=2)
video = cv2.VideoCapture(0)
time1 = 0
fall_detected = False
    
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    
    modified_frame, landmarks = detectPose(frame, pose_video, display=True)
    face_names = frr.recognize_face(frame)
    if face_names is not None:
        print("Detected faces:", face_names)
        
    time2 = time()
    
    if (time2 - time1) > 2: 
        # print("time")
        if landmarks is not None:
            # print("landmarks")
            height, _, _ = frame.shape
            fall_detected, previous_avg_shoulder_height = detectFall(landmarks, height, previous_avg_shoulder_height)
            if fall_detected:                 
                print("Fall detected!")          
        time1 = time2
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

video.release()
cv2.destroyAllWindows()
