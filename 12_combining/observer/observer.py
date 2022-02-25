import abc


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, duck):
        raise NotImplementedError('Abstract methods must be implemented')
