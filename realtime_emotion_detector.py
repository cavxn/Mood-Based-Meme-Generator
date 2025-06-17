import cv2
from generate_meme import get_meme_caption
from your_emotion_model import predict_emotion  # Replace with your model

# Initialize video capture
cap = cv2.VideoCapture(0)

last_emotion = ""
last_caption = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for consistent processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (48, 48))  # Ensure this matches your model
    emotion = predict_emotion(resized)

    # Only update caption if emotion changes
    if emotion != last_emotion:
        last_caption = get_meme_caption(emotion)
        last_emotion = emotion

    # Overlay caption on frame
    cv2.putText(frame, f"Emotion: {emotion}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
    cv2.putText(frame, last_caption, (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Mood-Based Meme Generator", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything
cap.release()
cv2.destroyAllWindows()
