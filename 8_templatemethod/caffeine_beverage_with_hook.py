import abc
from typing import final


class CaffeineBeverageWithHook:
    @final
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
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

    def customer_wants_condiments(self):
        return False
