# Mahir's Code

class Investment:
    def __init__(self, amount, returns):
        self.amount = amount
        self.returns = returns

    def calculate_roi(self):
        return (self.returns / self.amount) * 100
