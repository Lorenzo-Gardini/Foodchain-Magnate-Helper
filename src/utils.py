from src.player_model import Player

_UNIT_PRICE = 10
_MARKETER_INCREASE = 5
_WAITRESS = 3
_WAITRESS_INCREASE = 2

def compute_profit(player: Player,
                   pizzas: int,
                   burgers: int,
                   drinks: int,
                   waitress: int,
                   unit_price_modifier: int = 0) -> int:
    new_unit_price = _UNIT_PRICE + unit_price_modifier
    temp_profit = 0
    # pizzas
    temp_profit += pizzas * (new_unit_price + _MARKETER_INCREASE if player.pizza_marketer else 0)
    # burgers
    temp_profit += burgers * (new_unit_price + _MARKETER_INCREASE if player.burger_marketer else 0)
    # drinks
    temp_profit += drinks * (new_unit_price + _MARKETER_INCREASE if player.drink_marketer else 0)
    # waitress
    temp_profit +=  waitress * (_WAITRESS + _WAITRESS_INCREASE if player.firs_waitress_marketer else 0)
    # CFO
    temp_profit += temp_profit // 2
    return temp_profit