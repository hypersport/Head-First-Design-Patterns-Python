import abc
from quack_observable import QuackObservable


class Quackable(QuackObservable):
    @abc.abstractmethod
    def quack(self):
        raise NotImplementedError('Abstract methods must be implemented')
