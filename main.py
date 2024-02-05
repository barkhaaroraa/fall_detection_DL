import cv2
from cv2 import VideoCapture
import mediapipe as mp
import numpy as np
mp_drawing=mp.solutions.download_utils
mp_pose=mp.solutions.pose
cap=cv2.VideoCapture(0)
while cap.isOpened():
  ret,frame=cap.read()
  cv2.imshow('mediapipe feed',frame)
  if cv2.waitKey(10) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()