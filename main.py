import cv2
import mediapipe as mp
from time import time

previous_avg_eye_height = 0

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

def detectFall(landmarks, height, previous_avg_eye_height):
    # Extracting the y-coordinate of the eyes (landmark indices 27 and 32)
    left_eye_y = landmarks[11][1]
    right_eye_y = landmarks[12][1]
    
    # Calculate the average y-coordinate of the eyes
    avg_eye_y = (left_eye_y + right_eye_y) / 2

    if(previous_avg_eye_height==0):
        previous_avg_eye_height=avg_eye_y
        return False,previous_avg_eye_height

    
    # Threshold for fall detection (you can adjust this threshold as needed)
    fall_threshold = previous_avg_eye_height * 1.5
    print(previous_avg_eye_height, avg_eye_y,end="\n")
    
    # Check if the average eye y-coordinate falls less than 30% of the previous average eye height
    if avg_eye_y > fall_threshold:
        previous_avg_eye_height = avg_eye_y
        return True, previous_avg_eye_height
    else:
        previous_avg_eye_height = avg_eye_y
        return False, previous_avg_eye_height

pose_video = mp.solutions.pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=2)
video = cv2.VideoCapture(0)
time1 = 0
fall_detected = False
while video.isOpened():
    ret, frame = video.read()
    modified_frame, landmarks = detectPose(frame, pose_video, display=True)
    

    time2 = time()
    if (time2 - time1) > 4:  # Check every 5 seconds
        if landmarks is not None:
            height, _, _ = frame.shape
            fall_detected, previous_avg_eye_height = detectFall(landmarks, height, previous_avg_eye_height)
            if fall_detected:
                print("Fall detected!")
        time1 = time2

    # Display fall detection status on the frame
    # if fall_detected:
    #     # Draw red background rectangle
    #     cv2.rectangle(modified_frame, (0, 0), (300, 50), (0, 0, 255), -1)
    #     # Write "Fall Detected!" text on the rectangle
    #     cv2.putText(modified_frame, 'Fall Detected!', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    # cv2.imshow('Fall Detection', modified_frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

video.release()
cv2.destroyAllWindows()
