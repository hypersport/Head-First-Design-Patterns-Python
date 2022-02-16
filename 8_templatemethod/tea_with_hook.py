from caffeine_beverage_with_hook import CaffeineBeverageWithHook


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print('Steeping the tea.')

    def add_condiments(self):
        print('Adding Lemon.')

    def customer_wants_condiments(self):
        answer = input('Would you like lemon with your tea (y/n)? ')
        if answer.lower().startswith('y'):
            return True
        return False
