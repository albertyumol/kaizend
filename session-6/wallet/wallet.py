class InsufficientAmount(Exception):
    pass

class Wallet:
    balance = None

    def __init__(self, balance=None):
        self.balance = balance or 0


    def spend_cash(self, amount):
        #if amount > self.balance:
        #    raise InsufficientAmount('You do not have enough money.')
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount


