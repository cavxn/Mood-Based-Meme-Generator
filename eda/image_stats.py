import os
import cv2
import numpy as np

DATASET_PATH = "../images/images/train"
heights, widths = [], []

for emotion in os.listdir(DATASET_PATH):
    emotion_path = os.path.join(DATASET_PATH, emotion)
    for img_file in os.listdir(emotion_path):
        img_path = os.path.join(emotion_path, img_file)
        img = cv2.imread(img_path)
        if img is not None:
            h, w = img.shape[:2]
            heights.append(h)
            widths.append(w)

print(f"Total Images Analyzed: {len(heights)}")
print(f"Avg Height: {np.mean(heights):.2f} | Min: {min(heights)} | Max: {max(heights)}")
print(f"Avg Width : {np.mean(widths):.2f} | Min: {min(widths)} | Max: {max(widths)}")
