import os
import unittest
from typing import Dict, List

from dotenv import load_dotenv, find_dotenv

from src.player_model import PlayerStatus
from src.profit_calculator import compute_profit
from tests.utilities import generate_parameters_list

load_dotenv(find_dotenv())
UNIT_PRICE = int(os.getenv("UNIT_PRICE", 10))
MARKETER_INCREASE = int(os.getenv("MARKETER_INCREASE", 5))
WAITRESS = int(os.getenv("WAITRESS", 3))
WAITRESS_INCREASE = int(os.getenv("WAITRESS_INCREASE", 2))
SALARY_COST = int(os.getenv("SALARY_COST", 5))

class IntegrationTests(unittest.TestCase):
    _grid: List[Dict[str, int | bool]] = generate_parameters_list()

    def test_profit(self):
        for params in list(self._grid):
            player_status: PlayerStatus = PlayerStatus(**params)
            self.assertEqual(self._profit_calculator(player_status), compute_profit(player_status))


    @staticmethod
    def _profit_calculator(player_status: PlayerStatus) -> float:
        new_unit_price: int = UNIT_PRICE + player_status.unit_price_modifier
        burgers: int = player_status.burgers * (new_unit_price + MARKETER_INCREASE if player_status.has_burger_marketer else 0)
        pizzas: int = player_status.pizzas * (new_unit_price + MARKETER_INCREASE if player_status.has_pizza_marketer else 0)
        drinks: int = player_status.drinks * (new_unit_price + MARKETER_INCREASE if player_status.has_drink_marketer else 0)
        waitresses: int = player_status.waitress * (WAITRESS + WAITRESS_INCREASE if player_status.has_firs_waitress_marketer else 0)
        income = burgers + pizzas + drinks + waitresses
        if player_status.has_cfo:
            income += income // 2
        return income - player_status.salaries * SALARY_COST