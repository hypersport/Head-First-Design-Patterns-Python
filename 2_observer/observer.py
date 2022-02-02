import abc


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, temperature, humidity, pressure):
        raise Exception('Abstract methods must be implemented')
