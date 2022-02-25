from quack_observable import QuackObservable


class Observable(QuackObservable):
    def __init__(self, duck):
        self.duck = duck
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.duck)
