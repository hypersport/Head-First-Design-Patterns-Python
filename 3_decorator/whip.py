from condiment_decorator import CondimentDecorator
from beverage import Beverage


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        if isinstance(beverage, Beverage):
            self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self):
        return 0.10 + self.beverage.cost()
