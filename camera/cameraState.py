left_value = 17
right_value = 17

def update_camera_state(left: int, right: int):
    global left_value, right_value
    left_value = left
    right_value = right

def get_camera_state():
    return {
        "left": left_value,
        "right": right_value,
    }