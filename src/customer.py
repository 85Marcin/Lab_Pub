class Customer:
    def __init__(self, name, wallet, age, drunkeness) :
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def remove_money_from_wallet(self, amount):
        self.wallet -= amount

    def increase_drunkennes_level(self, alcohol_level):
        self.drunkeness += alcohol_level