import abc


class PizzaIngredientFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_dough(self):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def create_sauce(self):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def create_cheese(self):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def create_veggies(self):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def create_pepperoni(self):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def create_clam(self):
        raise Exception('Abstract methods must be implemented')
