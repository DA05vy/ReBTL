from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from App.models.leaf_lenet import lenet_leaf_model
from App.models.leaf_vgg import vgg_leaf_model
import numpy as np
from App.utils.image_preprocessing import preprocess_image

leaf_router = APIRouter()

@leaf_router.post("/lenet/inference")
async def lenet_inference(file: UploadFile = File(...)):
    """
    Inference ảnh với mô hình LeNet cho leaf.
    """
    try:
        img = await file.read()
        img_array = preprocess_image(img, target_size=(32, 32))  # LeNet
        pred = lenet_leaf_model.predict(img_array)
        result = int(np.argmax(pred, axis=1)[0])  # Nếu là classification nhiều lớp
        return JSONResponse(content={"prediction": result})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

@leaf_router.post("/vgg/inference")
async def vgg_inference(file: UploadFile = File(...)):
    """
    Inference ảnh với mô hình VGG cho leaf.
    """
    try:
        img = await file.read()
        img_array = preprocess_image(img, target_size=(224, 224))  # VGG
        pred = vgg_leaf_model.predict(img_array)
        result = int(np.argmax(pred, axis=1)[0])
        return JSONResponse(content={"prediction": result})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
