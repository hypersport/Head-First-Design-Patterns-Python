from Pyro5.api import Proxy
from gumball_monitor import GumballMonitor

if __name__ == '__main__':
    gumballMachine = Proxy('PYRO:example.GumballMachine@localhost:9999')
    gm = GumballMonitor(gumballMachine)
    gm.report()
