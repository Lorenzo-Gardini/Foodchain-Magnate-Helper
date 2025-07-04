from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.player_model import PlayerStatus
from src.profit_calculator import compute_profit

app = FastAPI(
    title="FCM helper",
    description="System for Food Chain Magnate, helping the player for profit calculation",
)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/profit_calculator")
async def profit_calculator(player_status: PlayerStatus = Query(...)):
    print(player_status)
    return {"profit": compute_profit(player_status)}
