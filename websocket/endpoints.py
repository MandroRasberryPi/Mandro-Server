import base64
import asyncio
import cv2
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

async def stream_camera(websocket: WebSocket, cam):
    await websocket.accept()
    try:
        while True:
            frame = cam.capture_array()
            frame = cv2.flip(frame, 1)
            _, jpeg = cv2.imencode(".jpg", frame)
            data = base64.b64encode(jpeg).decode("utf-8")
            await websocket.send_text(data)
            await asyncio.sleep(1 / 60)
    except WebSocketDisconnect:
        pass
