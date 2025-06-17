import os
import cv2

DATASET_PATH = "/Users/cavins/Desktop/project/Mood-Based-Meme-Generator/images/images/train"
corrupt_images = []

for emotion in os.listdir(DATASET_PATH):
    emotion_path = os.path.join(DATASET_PATH, emotion)
    for img_file in os.listdir(emotion_path):
        img_path = os.path.join(emotion_path, img_file)
        img = cv2.imread(img_path)
        if img is None:
            corrupt_images.append(img_path)

print(f"Corrupt images found: {len(corrupt_images)}")
for path in corrupt_images:
    print(path)
