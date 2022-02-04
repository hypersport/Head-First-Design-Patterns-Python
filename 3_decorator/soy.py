from condiment_decorator import CondimentDecorator
from beverage import Beverage


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        if isinstance(beverage, Beverage):
            self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Soy'

    def cost(self):
        self.size = self.beverage.get_size()
        cost = self.beverage.cost()
        if self.size == Beverage.Size.TALL:
            cost += 0.10
        elif self.size == Beverage.Size.GRANDE:
            cost += 0.15
        elif self.size == Beverage.Size.VENTI:
            cost += 0.20
        return cost
