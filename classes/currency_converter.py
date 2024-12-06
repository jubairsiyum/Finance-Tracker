# Shakib's Code

class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates  # rates is a dictionary with currency codes and conversion rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        return amount / self.rates[from_currency] * self.rates[to_currency]