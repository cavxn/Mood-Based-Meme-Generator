import os
import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# === Paths ===
model_path = "emotion_model.keras"
data_path = "images/images/preprocessed_data"
label_map_path = os.path.join(data_path, "label_map.pkl")

# === Load test data ===
X_test = np.load(os.path.join(data_path, "X_test.npy"))
y_test = np.load(os.path.join(data_path, "y_test.npy"))

# === Load model ===
model = tf.keras.models.load_model(model_path)

# === Predict on test data ===
y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

# === Load label map and invert it ===
with open(label_map_path, "rb") as f:
    label_map = pickle.load(f)
inv_label_map = {v: k for k, v in label_map.items()}
target_names = [inv_label_map[i] for i in range(len(inv_label_map))]

# === Classification report ===
report = classification_report(y_test, y_pred, target_names=target_names)
print("\n📊 Classification Report:\n")
print(report)

# === Confusion matrix ===
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt="d", xticklabels=target_names, yticklabels=target_names, cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.tight_layout()
plt.show()
