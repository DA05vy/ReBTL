import tensorflow as tf
import numpy as np
from App.shared.config import IMG_SIZE_LENET_LEAF

class LeNetLeafModel:
    def __init__(self):
        self.model = tf.keras.models.Sequential([
            # C1: Conv layer
            tf.keras.layers.Conv2D(
                filters=6, kernel_size=(5, 5), activation='relu', input_shape=(IMG_SIZE_LENET_LEAF, IMG_SIZE_LENET_LEAF, 3),
                padding='valid',  # mặc định
                name='conv2d_15'
            ),
            # S2: Average Pooling
            tf.keras.layers.AvgPool2D(
                pool_size=(2, 2), strides=(2, 2), padding='valid', name='average_pooling2d_2'
            ),
            # C3: Conv layer
            tf.keras.layers.Conv2D(
                filters=16, kernel_size=(5, 5), activation='relu', padding='valid', name='conv2d_16'
            ),
            # S4: Average Pooling
            tf.keras.layers.AvgPool2D(
                pool_size=(2, 2), strides=(2, 2), padding='valid', name='average_pooling2d_3'
            ),
            # Flatten
            tf.keras.layers.Flatten(name='flatten_2'),
            # C5: Fully connected
            tf.keras.layers.Dense(
                units=120, activation='relu', name='dense_6'
            ),
            # F6: Fully connected
            tf.keras.layers.Dense(
                units=84, activation='relu', name='dense_7'
            ),
            # Output layer
            tf.keras.layers.Dense(
                units=5, activation='softmax', name='dense_8'
            )
        ])
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        print(self.model.summary())

    def predict(self, img: np.ndarray): #TODO: Unknown logic
        """
        Dự đoán nhãn cho ảnh đầu vào.
        img: numpy array shape (1, IMG_SIZE_LENET_LEAF, IMG_SIZE_LENET_LEAF, 3)
        """
        preds = self.model.predict(img)
        # Nếu là binary classification, trả về 0 hoặc 1
        return (preds > 0.5).astype(int)


lenet_leaf_model = LeNetLeafModel()