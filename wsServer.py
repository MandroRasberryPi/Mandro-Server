import base64
import asyncio
import cv2
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect
from picamera2 import Picamera2
from libcamera import Transform

app = FastAPI()

picam0 = Picamera2(0)
picam0.configure(picam0.create_video_configuration(
    main={"size": (640, 480), "format": "RGB888"},
    transform=Transform(rotation=270)
))
picam0.set_controls({"AwbMode": 0, "ColourGains": (1.5, 1.9)})
picam0.start()

picam1 = Picamera2(1)
picam1.configure(picam1.create_video_configuration(
    main={"size": (640, 480), "format": "RGB888"},
    transform=Transform(rotation=90)
))
picam1.set_controls({"AwbMode": 0, "ColourGains": (1.5, 1.9)})
picam1.start()

@app.get("/")
async def index():
    with open("wsClient.html", "r") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws0")
async def websocket_cam0(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            frame = picam0.capture_array()
            frame = cv2.flip(frame, 1)
            _, jpeg = cv2.imencode(".jpg", frame)
            data = base64.b64encode(jpeg).decode("utf-8")
            await websocket.send_text(data)
            await asyncio.sleep(1 / 30)
    except WebSocketDisconnect:
        pass

@app.websocket("/ws1")
async def websocket_cam1(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            frame = picam1.capture_array()
            frame = cv2.flip(frame, 1)
            _, jpeg = cv2.imencode(".jpg", frame)
            data = base64.b64encode(jpeg).decode("utf-8")
            await websocket.send_text(data)
            await asyncio.sleep(1 / 30)
    except WebSocketDisconnect:
        pass
