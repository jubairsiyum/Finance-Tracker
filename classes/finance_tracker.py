# Siyum's Code
from classes.user import User
from classes.transaction import Transaction
from classes.category import Category

class FinanceTracker:
    def __init__(self, user):
        self.user = user
        self.transactions = []
        self.categories = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_total_expenses(self):
        return sum(t.amount for t in self.transactions if t.amount < 0)

    def set_goal(self, goal_amount, reward):
        self.goal = {"amount": goal_amount, "reward": reward}

    def generate_summary(self):
        return {
            "total_income": self.user.income,
            "total_expenses": self.get_total_expenses(),
            "net_balance": self.user.income + self.get_total_expenses()
        }
