import abc


class Quackable(metaclass=abc.ABCMeta):
    def quack(self):
        raise NotImplementedError('Abstract methods must be implemented')
