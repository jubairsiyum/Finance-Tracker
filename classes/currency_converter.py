# Shakib's Code

class CurrencyConverter:
    def __init__(self, rates=None):
        """
        Initialize the CurrencyConverter with optional dynamic rates.
        :param rates: Dictionary of dynamic rates (currency codes and conversion rates).
        """
        self.rates = rates or {}

    def convert(self, amount, from_currency, to_currency):
        """
        Convert an amount from one currency to another using dynamic rates.
        :param amount: The amount to convert.
        :param from_currency: The source currency code.
        :param to_currency: The target currency code.
        :return: Converted amount.
        """
        if from_currency == to_currency:
            return amount
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Currency rate not available for dynamic conversion.")
        return amount / self.rates[from_currency] * self.rates[to_currency]

    @staticmethod
    def static_convert(amount, from_currency, to_currency):
        """
        Convert an amount using predefined static conversion rates.
        :param amount: The amount to convert.
        :param from_currency: The source currency code.
        :param to_currency: The target currency code.
        :return: Converted amount.
        """
        static_rates = {
            ('USD', 'EUR'): 0.85,
            ('EUR', 'USD'): 1.18,
            ('USD', 'GBP'): 0.75,
            ('GBP', 'USD'): 1.33,
        }
        rate = static_rates.get((from_currency, to_currency), 1)
        return amount * rate


# Example Usage:
# Using dynamic rates
dynamic_rates = {'USD': 1, 'EUR': 0.85, 'GBP': 0.75}
converter = CurrencyConverter(dynamic_rates)
dynamic_result = converter.convert(100, 'USD', 'EUR')
print(f"Dynamic Conversion: 100 USD to EUR = {dynamic_result:.2f}")

# Using static rates
static_result = CurrencyConverter.static_convert(100, 'USD', 'GBP')
print(f"Static Conversion: 100 USD to GBP = {static_result:.2f}")
