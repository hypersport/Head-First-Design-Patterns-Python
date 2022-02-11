import abc


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def excuse(self):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def undo(self):
        raise Exception('Abstract methods must be implemented')
