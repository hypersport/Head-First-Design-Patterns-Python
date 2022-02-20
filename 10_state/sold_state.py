from state import State


class SoldState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print('Please wait, we\'re already giving you a gumball.')

    def eject_quarter(self):
        print('Sorry, you already turned the crank.')

    def turn_crank(self):
        print('Turning twice doesn\'t get you another gumball!')

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
        else:
            print('Oops, out of gumballs!')
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())

    def refill(self):
        pass

    def __str__(self):
        return 'dispensing a gumball.'
