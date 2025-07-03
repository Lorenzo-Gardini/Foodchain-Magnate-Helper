from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# app = FastAPI(
#     title="FCM helper",
#     description="System for Food Chain Magnate, helping the player in game",
# )
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Stato: connessioni e utenti
connected_users = {}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    connected_users[username] = websocket
    await broadcast_user_list()

    try:
        while True:
            data = await websocket.receive_text()
            # Puoi anche gestire messaggi qui
            pass
    except WebSocketDisconnect:
        del connected_users[username]
        await broadcast_user_list()


async def broadcast_user_list():
    user_list = list(connected_users.keys())
    for user_ws in connected_users.values():
        await user_ws.send_json({"type": "user_list", "users": user_list})
