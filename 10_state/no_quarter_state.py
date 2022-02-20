from state import State


class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print('You inserted a quarter.')
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())

    def eject_quarter(self):
        print('You haven\'t inserted a quarter.')

    def turn_crank(self):
        print('You turned, but there\'s no quarter.')

    def dispense(self):
        print('You need to pay first.')

    def refill(self):
        pass

    def __str__(self):
        return 'waiting for quarter.'
