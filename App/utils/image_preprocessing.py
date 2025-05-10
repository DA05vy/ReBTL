import numpy as np
from PIL import Image
import io

def preprocess_image(file_bytes: bytes, target_size: tuple) -> np.ndarray:
    """
    Tiền xử lý ảnh: resize, convert về array và normalize.
    """
    img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    img = img.resize(target_size)
    img_array = np.asarray(img) / 255.0  # Normalize
    return np.expand_dims(img_array, axis=0)
