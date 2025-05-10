import tensorflow as tf
import numpy as np
from App.shared.config import IMG_SIZE_LENET_ROCK

class LeNetRockModel:
    def __init__(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(filters=6, kernel_size=(5, 5), activation='relu', input_shape=(IMG_SIZE_LENET_ROCK, IMG_SIZE_LENET_ROCK, 3)),
            tf.keras.layers.AvgPool2D(pool_size=(2, 2), strides=2),
            tf.keras.layers.Conv2D(filters=16, kernel_size=(5, 5), activation='relu'),
            tf.keras.layers.AvgPool2D(pool_size=(2, 2), strides=2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(units=120, activation='relu'),
            tf.keras.layers.Dense(units=84, activation='relu'),
            tf.keras.layers.Dense(units=1, activation='sigmoid')
        ])

        print(self.model.summary())

    def load_model(self, model_path: str):

        self.model = tf.keras.models.load_model(model_path)
        print("")

    def predict(self, img: np.ndarray): #TODO: Unknown logic
        """
        Dự đoán nhãn cho ảnh đầu vào.
        img: numpy array shape (1, IMG_SIZE_LENET_ROCK, IMG_SIZE_LENET_ROCK, 3)
        """
        preds = self.model.predict(img)
        # Nếu là binary classification, trả về 0 hoặc 1
        return (preds > 0.5).astype(int)


lenet_rock_model = LeNetRockModel()