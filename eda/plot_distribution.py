import os
import seaborn as sns
import matplotlib.pyplot as plt

DATASET_PATH = "/Users/cavins/Desktop/project/Mood-Based-Meme-Generator/images/images/train"

emotion_counts = {emotion: len(os.listdir(os.path.join(DATASET_PATH, emotion)))
                  for emotion in os.listdir(DATASET_PATH)
                  if os.path.isdir(os.path.join(DATASET_PATH, emotion))}

plt.figure(figsize=(10, 6))
sns.barplot(x=list(emotion_counts.keys()), y=list(emotion_counts.values()), palette="viridis")
plt.title("Number of Images per Emotion Category")
plt.xlabel("Emotion")
plt.ylabel("Image Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("class_distribution.png")
plt.show()
