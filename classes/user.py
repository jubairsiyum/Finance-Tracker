class User:
    def __init__(self, name, income, currency, password):
        self.name = name
        self.income = income
        self.currency = currency
        self.password = password

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def authenticate(self, password):
        return self.password == password
