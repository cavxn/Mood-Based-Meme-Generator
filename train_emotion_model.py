import os
import numpy as np
import tensorflow as tf
import pickle
import json
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
import matplotlib.pyplot as plt

# === Load Preprocessed Data ===
data_path = "images/images/preprocessed_data"
X_train = np.load(os.path.join(data_path, "X_train.npy"))
y_train = np.load(os.path.join(data_path, "y_train.npy"))
X_val = np.load(os.path.join(data_path, "X_val.npy"))
y_val = np.load(os.path.join(data_path, "y_val.npy"))
X_test = np.load(os.path.join(data_path, "X_test.npy"))
y_test = np.load(os.path.join(data_path, "y_test.npy"))

# Expand grayscale to 3 channels (required for EfficientNet pretrained models)
X_train = np.repeat(X_train, 3, axis=-1)
X_val = np.repeat(X_val, 3, axis=-1)
X_test = np.repeat(X_test, 3, axis=-1)

# === Load Label Map ===
label_map_path = "images/images/preprocessed_data/label_map.pkl"
with open(label_map_path, "rb") as f:
    label_map = pickle.load(f)

num_classes = len(label_map)

# === Build EfficientNet Model ===
base_model = EfficientNetB0(include_top=False, input_shape=(48, 48, 3), weights="imagenet")
base_model.trainable = False  # Freeze base layers

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(num_classes, activation="softmax")
])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.summary()

# === Train the Model ===
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=64,
    verbose=1
)

# === Save the Model ===
model.save("emotion_model.keras")
print("✅ Model saved as emotion_model.keras")

# === Save Label Map as JSON for easier future use ===
with open("label_map.json", "w") as f:
    json.dump(label_map, f)
print("✅ Label map saved as label_map.json")

# === Plot Metrics ===
plt.figure(figsize=(12, 5))

# Accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()

# Loss
plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()

plt.tight_layout()
plt.show()
