from fastapi import FastAPI, WebSocket, Form, HTTPException
from fastapi.responses import JSONResponse
from routes.index import get_index_page
from websocket.endpoints import stream_camera
from camera.cameraManager import picam0, picam1
from camera.cameraState import update_camera_state, get_camera_state
from fastapi.middleware.cors import CORSMiddleware

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

@app.post("/update")
async def update_values(
    left: int = Form(...),
    right: int = Form(...),
):
    try:
        update_camera_state(left, right)
        return {"message": "Values updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/config")
async def get_config():
    state = get_camera_state()
    return state

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
