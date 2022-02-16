from caffeine_beverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    def brew(self):
        print('Steeping the tea.')

    def add_condiments(self):
        print('Adding Lemon.')
