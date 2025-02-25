import uvicorn
from fastapi import FastAPI
from routers import routers

if __name__ == '__main__':
    app = FastAPI()
    app.include_router(routers.router)
    uvicorn.run(app, host="127.0.0.1", port=8000)


