class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def remove_money_from_wallet(self, drink):
        self.wallet -= drink.price
