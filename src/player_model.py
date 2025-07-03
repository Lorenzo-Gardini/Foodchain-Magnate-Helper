

from dataclasses import dataclass
from typing import TypeAlias

PlayerId: TypeAlias = int

@dataclass
class Player:
    has_cfo: bool = False
    burger_marketer: bool = False
    pizza_marketer: bool = False
    drink_marketer: bool = False
    firs_waitress_marketer: bool = False
    total_profit: int = 0