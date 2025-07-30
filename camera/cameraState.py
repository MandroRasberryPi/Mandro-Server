left_value = 17
right_value = 17
distortion_level = 0.0

def update_camera_state(left: int, right: int, distortion_str: str):
    global left_value, right_value, distortion_level
    left_value = left
    right_value = right
    try:
        distortion_level = float(distortion_str)
    except:
        distortion_level = 0.0
    print(f"[UPDATE] left: {left}, right: {right}, distortion_level: {distortion_level}")

def get_camera_state():
    return {
        "left": left_value,
        "right": right_value,
        "distorted": distortion_level
    }