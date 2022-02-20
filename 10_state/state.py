import abc


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert_quarter(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def eject_quarter(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def turn_crank(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def dispense(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def refill(self):
        raise NotImplementedError('Abstract methods must be implemented')
