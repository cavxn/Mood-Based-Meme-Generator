import numpy as np
import matplotlib.pyplot as plt

# Assuming y_train is one-hot encoded, convert back to label indices
labels = np.argmax(y_train, axis=1)

# Plot class distribution
plt.figure(figsize=(8, 4))
plt.hist(labels, bins=np.arange(y_train.shape[1]+1)-0.5, rwidth=0.8)
plt.title("Class Distribution in y_train")
plt.xlabel("Emotion Label Index")
plt.ylabel("Count")
plt.xticks(range(y_train.shape[1]))
plt.show()
