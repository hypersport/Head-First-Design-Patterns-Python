from caffeine_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def brew(self):
        print('Dripping Coffee through filter.')

    def add_condiments(self):
        print('Adding Sugar and Milk.')
