from pydantic import BaseModel

class PlayerStatus(BaseModel):
    has_cfo: bool = False
    has_burger_marketer: bool = False
    has_pizza_marketer: bool = False
    has_drink_marketer: bool = False
    has_firs_waitress_marketer: bool = False
    pizzas: int = 0
    burgers: int = 0
    drinks: int = 0
    waitress: int = 0
    unit_price_modifier: int = 0
    salaries: int = 0