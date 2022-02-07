import abc


class Pizza(metaclass=abc.ABCMeta):
    name = ''

    clam = ''
    dough = ''
    sauce = ''
    cheese = ''
    pepperoni = ''
    veggies = []

    @abc.abstractmethod
    def prepare(self):
        raise Exception('Abstract methods must be implemented')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def bake(self):
        print('Baking ' + self.name)

    def cut(self):
        print('Cutting ' + self.name)

    def box(self):
        print('Boxing ' + self.name)

    def __str__(self):
        result = ['---- ' + self.get_name() + ' ----\n']
        if self.dough:
            result.append(str(self.dough))
            result.append('\n')
        if self.sauce:
            result.append(str(self.sauce))
            result.append('\n')
        if self.cheese:
            result.append(str(self.cheese))
            result.append('\n')
        if self.veggies:
            for veggie in self.veggies:
                result.append(str(veggie))
                if veggie != self.veggies[-1]:
                    result.append(', ')
            result.append('\n')
        if self.clam:
            result.append(str(self.clam))
            result.append('\n')
        if self.pepperoni:
            result.append(str(self.pepperoni))
            result.append('\n')
        return ''.join(result)
