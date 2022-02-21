from Pyro5.api import expose
from Pyro5.api import behavior


@expose
@behavior(instance_mode='single')
class GumballMachine:
    def __init__(self, location='Earth', number_gumballs=10):
        self.count = number_gumballs
        self.location = location

    def get_count(self):
        return self.count

    def get_location(self):
        return self.location

    def __str__(self):
        result = ['\nMighty Gumball, Inc.', f'\nInventory: {self.count} gumball']
        if self.count != 1:
            result.append('s')
        result.append(f'\nMachine is {self.state}\n')
        return ''.join(result)
