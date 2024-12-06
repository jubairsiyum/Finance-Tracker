# Shakib's Code

class TaxCalculator:
    def __init__(self, tax_rate):
        """
        Initializes with a tax rate percentage.
        """
        self.tax_rate = tax_rate

    def calculate_tax(self, amount):
        """
        Calculates the tax based on the amount and the tax rate.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount * self.tax_rate / 100  # Calculate the tax

    def __repr__(self):
        """String representation of the TaxCalculator."""
        return f"TaxCalculator(tax_rate={self.tax_rate}%)"
