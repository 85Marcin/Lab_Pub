class Customer:
    def __init__(self, name, wallet, age, drunkenness) :
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def remove_money_from_wallet(self, amount):
        self.wallet -= amount

    def increase_drunkenness_level(self, alcohol_level):
        self.drunkenness += alcohol_level