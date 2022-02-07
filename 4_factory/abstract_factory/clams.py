import abc


class Clams(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self):
        raise Exception('Abstract methods must be implemented')
