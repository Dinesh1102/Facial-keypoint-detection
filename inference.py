import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model('trained_model.h5')

input_size = (96, 96)
scale_factor = 1.0 / 255

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_img = gray[y:y + h, x:x + w]
        face_resized = cv2.resize(face_img, input_size)
        face_normalized = face_resized * scale_factor
        face_input = np.expand_dims(face_normalized, axis=(0, -1))  # Shape: (1, h, w, 1)

        # Predict keypoints
        keypoints = model.predict(face_input)[0]  # Shape: (num_keypoints*2,)
        # print(keypoints)
        for i in range(0, len(keypoints), 2):
            x_coord = int(keypoints[i] * w / input_size[0]) + x
            y_coord = int(keypoints[i + 1] * h / input_size[1]) + y
            cv2.circle(frame, (x_coord, y_coord), 2, (0, 255, 0), -1)

    cv2.imshow('Facial Keypoint Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()