import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import CSVLogger
from resnet_cbam_model import build_model

# Load data
DATA_DIR = "images/images/preprocessed_data"
X_train = np.load(f"{DATA_DIR}/X_train.npy")
y_train = np.load(f"{DATA_DIR}/y_train.npy")
X_val = np.load(f"{DATA_DIR}/X_val.npy")
y_val = np.load(f"{DATA_DIR}/y_val.npy")

# Load label map
with open(f"{DATA_DIR}/label_map.pkl", "rb") as f:
    label_map = pickle.load(f)
num_classes = len(label_map)

# One-hot encode
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_val = tf.keras.utils.to_categorical(y_val, num_classes)

# Build & compile model
model = build_model(input_shape=(48, 48, 1), num_classes=num_classes)
model.compile(optimizer=Adam(1e-3), loss='categorical_crossentropy', metrics=['accuracy'])

# Train
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50, batch_size=64, verbose=1,
                    callbacks=[CSVLogger("training_log.csv")])

# Save model and label map
model.save("emotion_model_cbam.keras")
with open("label_map.json", "w") as f:
    import json
    json.dump(label_map, f)

print("✅ Model trained and saved.")
