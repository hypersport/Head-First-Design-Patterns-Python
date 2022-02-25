import abc


class AbstractDuckFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_mallard_duck(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def create_redhead_duck(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def create_duck_call(self):
        raise NotImplementedError('Abstract methods must be implemented')

    @abc.abstractmethod
    def create_rubber_duck(self):
        raise NotImplementedError('Abstract methods must be implemented')
