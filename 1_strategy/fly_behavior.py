import abc


class FlyBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        raise Exception('Abstract methods must be implemented')
