from fastapi.responses import HTMLResponse

def get_index_page():
    with open("static/wsClient.html", "r") as f:
        return HTMLResponse(f.read())
