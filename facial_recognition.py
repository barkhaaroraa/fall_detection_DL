import face_recognition
import os
import cv2
import numpy as np

class FaceRecognition:
    def __init__(self):
        self.known_faces = []
        self.known_face_names = []

    def encode_faces(self):
        for image in os.listdir('pictures'):
            face_image = face_recognition.load_image_file(f'pictures/{image}')
            face_encodings = face_recognition.face_encodings(face_image)[0]

            self.known_faces.append(face_encodings)
            self.known_face_names.append(image)
            print(self.known_face_names)

    def recognize_face(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_faces, face_encoding)
            name = 'unknown'
            confidence = 'unknown'
            face_distances = face_recognition.face_distance(self.known_faces, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                return name
            face_names.append(name)

# fr = FaceRecognition()
# fr.encode_faces()

# video = cv2.VideoCapture('video3.mp4')
# if not video.isOpened():
#     print("Error: Unable to open camera.")
#     exit()

# while True:
#     ret, frame = video.read()
#     if not ret:
#         print("Error: Unable to capture frame.")
#         break

#     name = fr.recognize_face(frame)
#     if name:
#         print(f"Detected: {name}")

#     cv2.imshow('Frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()
