from picamera2 import Picamera2
from libcamera import Transform

def create_camera(index: int, rotation: int) -> Picamera2:
    cam = Picamera2(index)
    cam.configure(cam.create_video_configuration(
        main={"size": (640, 480), "format": "RGB888"},
        transform=Transform(rotation=rotation)
    ))
    cam.set_controls({"AwbMode": 0, "ColourGains": (1.5, 1.9)})
    cam.start()
    return cam

picam0 = create_camera(0, 270)
picam1 = create_camera(1, 90)