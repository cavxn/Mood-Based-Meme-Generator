import tensorflow as tf

model = tf.keras.models.load_model("emotion_model_cbam.keras", compile=False)

# TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open("emotion_model.tflite", "wb") as f:
    f.write(tflite_model)

# ONNX (requires tf2onnx)
# pip install tf2onnx
import tf2onnx
spec = (tf.TensorSpec((None, 48, 48, 1), tf.float32),)
model_proto, _ = tf2onnx.convert.from_keras(model, input_signature=spec, opset=13, output_path="emotion_model.onnx")

print("✅ Model converted to TFLite and ONNX.")
