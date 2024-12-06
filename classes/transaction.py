# Siyum's Code
class Transaction:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
