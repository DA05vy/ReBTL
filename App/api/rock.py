from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from App.models.rock_lenet import LeNetRockModel
from App.models.rock_vgg import vgg_rock_model
from App.utils.image_preprocessing import preprocess_image

rock_router = APIRouter()
lenet_model = LeNetRockModel()
vgg_model = vgg_rock_model

@rock_router.post("/lenet/inference")
async def lenet_inference(file: UploadFile = File(...)):
    try:
        img = preprocess_image(file, target_size=(32, 32))
        pred = lenet_model.predict(img)
        return {"prediction": pred}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

@rock_router.post("/vgg/inference")
async def vgg_inference(file: UploadFile = File(...)):
    try:
        img = preprocess_image(file, target_size=(150, 150))
        pred = vgg_model.predict(img)
        return {"prediction": pred}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
