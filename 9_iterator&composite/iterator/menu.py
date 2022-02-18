import abc


class Menu(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_iterator(self):
        raise Exception('Abstract methods must be implemented')
