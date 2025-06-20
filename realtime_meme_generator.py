# realtime_meme_generator.py

import cv2
import numpy as np
import tensorflow as tf
import pickle
from generate_meme import get_meme_caption

# Load model and labels
model = tf.keras.models.load_model("emotion_model.keras")
with open("label_map.pkl", "rb") as f:
    label_map = pickle.load(f)
inv_label_map = {v: k for k, v in label_map.items()}

cap = cv2.VideoCapture(0)
IMG_SIZE = 48
last_emotion = None
last_caption = ""

def preprocess_face(face):
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (IMG_SIZE, IMG_SIZE))
    normalized = resized.astype("float32") / 255.0
    return np.expand_dims(normalized[..., np.newaxis], axis=0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        input_data = preprocess_face(face_roi)
        prediction = model.predict(input_data, verbose=0)
        emotion = inv_label_map[np.argmax(prediction)]

        if emotion != last_emotion:
            last_emotion = emotion
            last_caption = get_meme_caption(emotion)
            print(f"Detected emotion: {emotion}, Meme: {last_caption}")

        # Draw box and caption
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, last_caption, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Meme Generator", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
