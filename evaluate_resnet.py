import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# === Load the saved model and label map ===
model = tf.keras.models.load_model("emotion_model.keras")
with open("label_map.pkl", "rb") as f:
    label_map = pickle.load(f)
class_names = list(label_map.keys())

# === Load test data ===
X_test = np.load("images/images/preprocessed_data/X_test.npy")
y_test = np.load("images/images/preprocessed_data/y_test.npy")

# === Predict and evaluate ===
y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

# === Metrics ===
accuracy = np.mean(y_pred == y_test)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

print("✅ Evaluation Metrics:")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

# === Classification Report ===
print("\n📄 Classification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

# === Confusion Matrix ===
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=class_names, yticklabels=class_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
