# Siyum's Code:
import numpy as np

class Category:
    def __init__(self, name, budget_limit=0.0):
        self.name = name
        self.budget_limit = budget_limit
        self.expenses = np.array([])  # Use a NumPy array for expenses

    def get_name(self):
        return self.name

    def set_budget_limit(self, limit):
        self.budget_limit = limit

    def add_expense(self, amount):
        self.expenses = np.append(self.expenses, amount)  # Add new expense to the array

    def total_expenses(self):
        return np.sum(self.expenses)  # Use NumPy's sum function for efficient summation

    def average_expenses(self):
        return np.mean(self.expenses)  # Calculate the average expense

    def remaining_budget(self):
        return self.budget_limit - np.sum(self.expenses)  # Calculate the remaining budget

    def expense_summary(self):
        return {
            "total_expenses": self.total_expenses(),
            "average_expense": self.average_expenses(),
            "remaining_budget": self.remaining_budget()
        }
