from Pyro5.api import Daemon
from gumball_machine import GumballMachine

if __name__ == '__main__':
    Daemon.serveSimple(
        {GumballMachine: 'example.GumballMachine'},
        host='localhost',
        port=9999,
        ns=False,
        verbose=True
    )
