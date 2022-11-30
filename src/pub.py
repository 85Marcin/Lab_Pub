class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drink_to_menu(self, drink):
        self.drinks.append(drink)
        
    def add_money_to_till(self, amount):
        self.till += amount

    def sell_drink(self, drink):
        self.till += drink.price
        