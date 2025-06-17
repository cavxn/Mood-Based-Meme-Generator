import os
from collections import defaultdict

DATASET_PATH = "/Users/cavins/Desktop/project/Mood-Based-Meme-Generator/images/images/train"

emotion_counts = defaultdict(int)

for emotion in os.listdir(DATASET_PATH):
    emotion_path = os.path.join(DATASET_PATH, emotion)
    if os.path.isdir(emotion_path):
        emotion_counts[emotion] = len(os.listdir(emotion_path))

print("Image count per emotion:\n")
for emotion, count in sorted(emotion_counts.items()):
    print(f"{emotion}: {count}")
