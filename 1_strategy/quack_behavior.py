import abc


class QuackBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        raise Exception('Abstract methods must be implemented')
