import abc
import enum


class Beverage(metaclass=abc.ABCMeta):
    class Size(enum.Enum):
        TALL = 1
        GRANDE = 2
        VENTI = 3

    description = 'Unknown Beverage'
    size = Size.TALL

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_description(self):
        return self.description

    def cost(self):
        pass
