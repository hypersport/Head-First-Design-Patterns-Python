from quack_behavior import QuackBehavior


class FakeQuack(QuackBehavior):
    def quack(self):
        print('Qwak')
