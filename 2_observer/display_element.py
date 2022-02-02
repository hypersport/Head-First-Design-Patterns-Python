import abc


class DisplayElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        raise Exception('Abstract methods must be implemented')
