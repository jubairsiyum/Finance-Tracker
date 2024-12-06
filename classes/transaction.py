# Siyum's Code
import numpy as np

class Transaction:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount


class TransactionManager:
    def __init__(self):
        self.transactions = np.array([])  # Store transactions in a NumPy array

    def add_transaction(self, transaction):
        self.transactions = np.append(self.transactions, transaction)  # Add new transaction

    def total_transactions(self):
        return np.sum([t.get_amount() for t in self.transactions])  # Sum of all transaction amounts

    def filter_transactions_by_category(self, category_name):
        return [t for t in self.transactions if t.category == category_name]  # Filter transactions by category

    def average_transaction(self):
        return np.mean([t.get_amount() for t in self.transactions])  # Calculate average transaction

    def transaction_summary(self):
        return {
            "total_transactions": self.total_transactions(),
            "average_transaction": self.average_transaction(),
        }
