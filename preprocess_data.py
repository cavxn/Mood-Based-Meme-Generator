# preprocess_dataset.py

import os
import cv2
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Configuration
IMG_SIZE = 48
DATASET_PATH = "/Users/cavins/Desktop/project/Mood-Based-Meme-Generator/images/images/train"  # Relative path from script
TEST_SPLIT = 0.1
VAL_SPLIT = 0.1

# Load and preprocess images
X, y = [], []
class_names = sorted(os.listdir(DATASET_PATH))
label_map = {emotion: idx for idx, emotion in enumerate(class_names)}

for emotion in class_names:
    emotion_path = os.path.join(DATASET_PATH, emotion)
    for img_name in os.listdir(emotion_path):
        img_path = os.path.join(emotion_path, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (IMG_SIZE, IMG_SIZE))
        X.append(resized)
        y.append(label_map[emotion])

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1).astype("float32") / 255.0
y = np.array(y)

# Split into train, val, test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=TEST_SPLIT, stratify=y, random_state=42)
val_size_adjusted = VAL_SPLIT / (1 - TEST_SPLIT)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=val_size_adjusted, stratify=y_temp, random_state=42)

print(f"✅ Shapes — Train: {X_train.shape}, Val: {X_val.shape}, Test: {X_test.shape}")

# Plot class distribution
plt.figure(figsize=(8, 4))
plt.hist(y_train, bins=np.arange(y_train.max()+2)-0.5, rwidth=0.8)
plt.title("Class Distribution in y_train")
plt.xlabel("Emotion Label Index")
plt.ylabel("Count")
plt.xticks(range(int(y_train.max())+1))
plt.grid(True)
plt.tight_layout()
plt.show()

# Save all data in one file
np.savez_compressed("preprocessed_data.npz",
                    X_train=X_train, y_train=y_train,
                    X_val=X_val, y_val=y_val,
                    X_test=X_test, y_test=y_test)

# Save label map
with open("label_map.pkl", "wb") as f:
    pickle.dump(label_map, f)

print("✅ Preprocessing complete. Saved as preprocessed_data.npz and label_map.pkl")
