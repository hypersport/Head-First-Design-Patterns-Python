import abc


class Turkey(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gobble(self):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def fly(self):
        raise Exception('Abstract methods must be implemented')
