import abc


class QuackObservable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_observer(self, observer):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def notify_observers(self):
        raise NotImplementedError('Abstract methods must be implemented')
