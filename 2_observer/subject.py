import abc


class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_observer(self, observer):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def remove_observer(self, observer):
        raise Exception('Abstract methods must be implemented')

    @abc.abstractmethod
    def notify_observers(self):
        raise Exception('Abstract methods must be implemented')
