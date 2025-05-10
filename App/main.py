from __future__ import annotations

from api.rock import rock_router
from api.leaf import leaf_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Inference model', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(rock_router, prefix='/api/rock', tags=['rock'])
app.include_router(leaf_router, prefix='/api/leaf', tags=['leaf'])

if __name__ == "__main__":
    import uvicorn

    # Start the server
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True, log_level="debug")
