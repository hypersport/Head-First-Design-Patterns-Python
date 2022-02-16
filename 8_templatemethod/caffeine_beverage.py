import abc
from typing import final


class CaffeineBeverage(metaclass=abc.ABCMeta):
    @final
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abc.abstractmethod
    def brew(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def add_condiments(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @staticmethod
    def boil_water():
        print('Boiling water.')

    @staticmethod
    def pour_in_cup():
        print('Pouring into cup.')
