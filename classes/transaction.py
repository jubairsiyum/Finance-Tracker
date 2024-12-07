# Siyum's Code
import numpy as np

from classes.notification_system import NotificationSystem


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
        NotificationSystem.set_notification("Test")

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

"""class TransactionManager:
    def __init__(self):
        # Transactions array, each row: (amount, category, date)
        self.transactions = np.array([])

    def add_transaction(self, transaction):
         Add a new transaction to the transactions array. 
        # Convert transaction into an array (amount, category, date)
        transaction_data = np.array([(transaction.amount, transaction.category, transaction.date)])
        # Append the transaction data to the existing transactions array
        self.transactions = np.append(self.transactions, transaction_data, axis=0)

    def total_transactions(self):
         Sum all transaction amounts using NumPy vectorized operation. 
        if self.transactions.size == 0:
            return 0  # Return 0 if there are no transactions
        # Using NumPy to sum the amounts (0th column in the array)
        return np.sum(self.transactions[:, 0])  # transactions[:, 0] accesses the amounts

    def filter_transactions_by_category(self, category_name):
        " Filter transactions by category using NumPy's boolean indexing. 
        if self.transactions.size == 0:
            return []  # Return an empty list if no transactions
        # Use NumPy boolean indexing to filter by category (1st column in the array)
        filtered_transactions = self.transactions[self.transactions[:, 1] == category_name]
        return filtered_transactions

    def average_transaction(self):
         Calculate the average transaction amount using NumPy. 
        if self.transactions.size == 0:
            return 0  # Return 0 if there are no transactions
        # Calculate the average of the amounts (0th column)
        return np.mean(self.transactions[:, 0])

    def transaction_summary(self):
         Return the summary of all transactions including total and average.
        return {
            "total_transactions": self.total_transactions(),
            "average_transaction": self.average_transaction(),
        }"""
