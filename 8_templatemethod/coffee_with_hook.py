from caffeine_beverage_with_hook import CaffeineBeverageWithHook


class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print('Dripping Coffee through filter.')

    def add_condiments(self):
        print('Adding Sugar and Milk.')

    def customer_wants_condiments(self):
        answer = input('Would you like milk and sugar with your coffee (y/n)? ')
        if answer.lower().startswith('y'):
            return True
        return False
