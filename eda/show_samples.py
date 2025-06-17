import os
import cv2
import matplotlib.pyplot as plt

DATASET_PATH = "../images/images/train"
SAMPLES_PER_CLASS = 5

emotions = sorted(os.listdir(DATASET_PATH))
fig, axes = plt.subplots(len(emotions), SAMPLES_PER_CLASS, figsize=(SAMPLES_PER_CLASS * 2, len(emotions) * 2))

for i, emotion in enumerate(emotions):
    emotion_path = os.path.join(DATASET_PATH, emotion)
    image_files = os.listdir(emotion_path)[:SAMPLES_PER_CLASS]
    for j, img_name in enumerate(image_files):
        img_path = os.path.join(emotion_path, img_name)
        img = cv2.imread(img_path)
        
        if img is None:
            print(f"[⚠️] Skipping unreadable image: {img_path}")
            axes[i, j].axis('off')
            axes[i, j].set_title("Invalid")
            continue

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        axes[i, j].imshow(img)
        axes[i, j].axis('off')
        if j == 0:
            axes[i, j].set_title(emotion, fontsize=10)

plt.tight_layout()
plt.suptitle("Sample Images per Emotion", fontsize=16)
plt.subplots_adjust(top=0.95)
plt.savefig("sample_images.png")
plt.show()
