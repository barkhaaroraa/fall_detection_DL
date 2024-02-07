import cv2
import mediapipe as mp
from time import time
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
pose_video = mp.solutions.pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=2)
video = cv2.VideoCapture(0)
time1 = 0
while video.isOpened():
    ret, frame = video.read()
    modified_frame, _ = detectPose(frame, pose_video, display=True)

    time2 = time()
    if (time2 - time1) > 0:
        frames_per_second = 1.0 / (time2 - time1)
        cv2.putText(modified_frame, 'FPS: {}'.format(int(frames_per_second)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

    time1 = time2
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
video.release()
cv2.destroyAllWindows()
