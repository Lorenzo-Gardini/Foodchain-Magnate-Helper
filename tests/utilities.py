from typing import Dict, List

from sklearn.model_selection import ParameterGrid


def generate_parameters_list()-> List[Dict[str, int | bool]]:
    return list(ParameterGrid(param_grid={
        'has_cfo': [True, False],
        'has_burger_marketer': [True, False],
        'has_pizza_marketer': [True, False],
        'has_drink_marketer': [True, False],
        'has_firs_waitress_marketer': [True, False],
        'pizzas': [0, 5],
        'burgers': [0, 5],
        'drinks': [0, 5],
        'waitress': [0, 3, 5],
        'unit_price_modifier': [0, -1, +10],
        'salaries': [0, 3, 5],
    }))