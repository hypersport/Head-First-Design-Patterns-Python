from state import State


class WinnerState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print('Please wait, we\'re already giving you a gumball.')

    def eject_quarter(self):
        print('Please wait, we\'re already giving you a Gumball.')

    def turn_crank(self):
        print('Turning again doesn\'t get you another gumball!')

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() == 0:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
        else:
            self.gumball_machine.release_ball()
            print('YOU\'RE A WINNER! You got two gumballs for your quarter')
            if self.gumball_machine.get_count() > 0:
                self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
            else:
                print('Oops, out of gumballs!')
                self.gumball_machine.set_state(self.gumball_machine.set_sold_out_state())

    def refill(self):
        pass

    def __str__(self):
        return 'despensing two gumballs for your quarter, because YOU\'RE A WINNER!'
