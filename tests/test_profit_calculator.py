import os
import unittest
from itertools import combinations
from typing import Dict, List, Set, Collection, Any

from dotenv import load_dotenv, find_dotenv
from fastapi.testclient import TestClient
from main import app
from src.profit_calculator import compute_profit
from src.player_model import PlayerStatus

load_dotenv(find_dotenv())
UNIT_PRICE = int(os.getenv("UNIT_PRICE", 10))
MARKETER_INCREASE = int(os.getenv("MARKETER_INCREASE", 5))
WAITRESS = int(os.getenv("WAITRESS", 3))
WAITRESS_INCREASE = int(os.getenv("WAITRESS_INCREASE", 2))
SALARY_COST = int(os.getenv("SALARY_COST", 5))

class IntegrationTests(unittest.TestCase):
    _client: TestClient = TestClient(app)

    def test_burgers(self):
        pass

