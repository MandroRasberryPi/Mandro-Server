from fastapi import FastAPI, WebSocket
from routes.index import get_index_page
from websocket.endpoints import stream_camera
from camera.cameraManager import picam0, picam1

app = FastAPI()

@app.get("/")
async def index():
    return get_index_page()

@app.websocket("/ws0")
async def websocket_cam0(websocket: WebSocket):
    await stream_camera(websocket, picam0)

@app.websocket("/ws1")
async def websocket_cam1(websocket: WebSocket):
    await stream_camera(websocket, picam1)
