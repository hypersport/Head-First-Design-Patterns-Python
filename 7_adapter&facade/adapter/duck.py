import abc


class Duck(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def fly(self):
        raise Exception('Abstract methods must be implemented')
