import abc
from beverage import Beverage


class CondimentDecorator(Beverage, metaclass=abc.ABCMeta):
    beverage = None

    def get_description(self):
        pass

    def get_size(self):
        self.beverage.get_size()
