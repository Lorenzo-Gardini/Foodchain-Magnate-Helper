import os

from src.player_model import PlayerStatus
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


UNIT_PRICE: int = int(os.getenv("UNIT_PRICE", 10))
MARKETER_INCREASE: int = int(os.getenv("MARKETER_INCREASE", 5))
WAITRESS: int = int(os.getenv("WAITRESS", 3))
WAITRESS_INCREASE: int = int(os.getenv("WAITRESS_INCREASE", 2))
SALARY_COST: int = int(os.getenv("SALARY_COST", 5))

def compute_profit(player_status: PlayerStatus) -> int:
    new_unit_price: int  = UNIT_PRICE + player_status.unit_price_modifier
    temp_profit: int = 0
    # pizzas
    temp_profit += player_status.pizzas * (new_unit_price + MARKETER_INCREASE if player_status.has_pizza_marketer else 0)
    # burgers
    temp_profit += player_status.burgers * (new_unit_price + MARKETER_INCREASE if player_status.has_burger_marketer else 0)
    # drinks
    temp_profit += player_status.drinks * (new_unit_price + MARKETER_INCREASE if player_status.has_drink_marketer else 0)
    # waitress
    temp_profit +=  player_status.waitress * (WAITRESS + WAITRESS_INCREASE if player_status.has_firs_waitress_marketer else 0)
    # CFO
    temp_profit += temp_profit // 2
    # salaries
    temp_profit -= player_status.salaries * SALARY_COST
    return temp_profit