import abc


class Quackable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        raise NotImplementedError('Abstract methods must be implemented')
