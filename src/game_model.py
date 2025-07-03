import copy
from enum import Enum
from typing import Dict

from src.player_model import PlayerId, Player


class GamePhase(Enum):
    FirstPhase = 0
    SecondPhase = 1


class GameModel:
    _UNITS_FOR_PLAYER_FIRST_BANK = 50
    def __init__(self, players_amount: int) -> None:
        self._current_amount: int = self._UNITS_FOR_PLAYER_FIRST_BANK * players_amount
        self._game_phase: GamePhase = GamePhase.FirstPhase

    def fill_second_time(self, quantity: int):
        if self._game_phase != GamePhase.FirstPhase or self._current_amount <= 0:
            raise Exception("Game phase must be first phase")
        self._current_amount +=quantity

    @property
    def current_amount(self) -> int:
        return self._current_amount
    
    def subtract_amount(self, amount: int):
        self._current_amount -= amount

    @property
    def is_game_over(self) -> bool:
        return self._game_phase == GamePhase.SecondPhase and self._current_amount <= 0


