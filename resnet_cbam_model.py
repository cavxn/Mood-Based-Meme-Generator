# resnet_cbam_model.py

import tensorflow as tf
from tensorflow.keras.layers import Layer, Conv2D, Dense, GlobalAveragePooling2D, GlobalMaxPooling2D, Reshape, Multiply, Add, Activation, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Input

class CBAM(Layer):
    def __init__(self, reduction_ratio=8, **kwargs):
        super(CBAM, self).__init__(**kwargs)
        self.reduction_ratio = reduction_ratio

    def build(self, input_shape):
        channel = input_shape[-1]
        self.shared_dense_one = Dense(channel // self.reduction_ratio, activation='relu', kernel_initializer='he_normal', use_bias=True)
        self.shared_dense_two = Dense(channel, kernel_initializer='he_normal', use_bias=True)

        self.conv_spatial = Conv2D(filters=1, kernel_size=7, strides=1, padding='same', activation='sigmoid', kernel_initializer='he_normal', use_bias=False)

    def call(self, inputs):
        # Channel attention
        avg_pool = GlobalAveragePooling2D()(inputs)
        max_pool = GlobalMaxPooling2D()(inputs)

        avg_pool = Reshape((1, 1, -1))(avg_pool)
        max_pool = Reshape((1, 1, -1))(max_pool)

        mlp_avg = self.shared_dense_two(self.shared_dense_one(avg_pool))
        mlp_max = self.shared_dense_two(self.shared_dense_one(max_pool))

        channel_attention = Activation('sigmoid')(Add()([mlp_avg, mlp_max]))
        channel_refined = Multiply()([inputs, channel_attention])

        # Spatial attention
        avg_pool_spatial = tf.reduce_mean(channel_refined, axis=-1, keepdims=True)
        max_pool_spatial = tf.reduce_max(channel_refined, axis=-1, keepdims=True)
        spatial_attention = Concatenate(axis=-1)([avg_pool_spatial, max_pool_spatial])

        spatial_attention = self.conv_spatial(spatial_attention)
        refined_feature = Multiply()([channel_refined, spatial_attention])

        return refined_feature

def build_model(input_shape=(48, 48, 1), num_classes=7):
    inputs = Input(shape=input_shape)

    # Upscale to 3 channels for ResNet50
    x = Conv2D(3, (1, 1), padding='same')(inputs)

    base_model = ResNet50(include_top=False, input_tensor=x, weights=None, pooling=None)

    x = base_model.output
    x = CBAM()(x)
    x = GlobalAveragePooling2D()(x)
    outputs = Dense(num_classes, activation='softmax')(x)

    return Model(inputs, outputs)
