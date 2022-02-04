from condiment_decorator import CondimentDecorator
from beverage import Beverage


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        if isinstance(beverage, Beverage):
            self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        return 0.20 + self.beverage.cost()
