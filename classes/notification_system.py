# Shakib's Code

# Notification Class
class Notification:
    def __init__(self):
        self.notifications = []

    def add_notification(self, message):
        self.notifications.append(message)

    def get_notifications(self):
        return self.notifications

    def clear_notifications(self):
        self.notifications.clear()

# Category Class
class Category(Notification):
    def __init__(self):
        super().__init__()
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)
        self.add_notification(f"Category '{category}' added.")

    def remove_category(self, category):
        if category in self.categories:
            self.categories.remove(category)
            self.add_notification(f"Category '{category}' removed.")
        else:
            self.add_notification(f"Error: Category '{category}' not found.")

    def __repr__(self):
        return f"Category(categories={self.categories})"

# CurrencyConverter Class
class CurrencyConverter(Notification):
    def __init__(self, rates):
        super().__init__()
        self.rates = rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            self.add_notification(f"Error: Conversion rate not found for '{from_currency}' to '{to_currency}'.")
            raise ValueError("Conversion rate not found.")
        converted_amount = amount * (self.rates[to_currency] / self.rates[from_currency])
        self.add_notification(f"Converted {amount} {from_currency} to {converted_amount:.2f} {to_currency}.")
        return converted_amount

# GoalReward Class
class GoalReward(Notification):
    def __init__(self, goal_name, target_amount):
        super().__init__()
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.current_amount = 0
        self.add_notification(f"Goal '{goal_name}' created with target of {target_amount}.")

    def add_to_goal(self, amount):
        self.current_amount += amount
        self.add_notification(f"Added {amount} to goal '{self.goal_name}'. Current amount: {self.current_amount}.")

    def __repr__(self):
        return f"GoalReward(goal_name={self.goal_name}, target={self.target_amount}, current={self.current_amount})"

# Investment Class
class Investment(Notification):
    def __init__(self, name, principal, rate):
        super().__init__()
        self.name = name
        self.principal = principal
        self.rate = rate
        self.add_notification(f"Investment '{name}' created with principal {principal} and rate {rate}%.")

    def calculate_return(self, years):
        total_return = self.principal * ((1 + (self.rate / 100)) ** years)
        self.add_notification(f"Return for investment '{self.name}' over {years} years: {total_return:.2f}.")
        return total_return

    def __repr__(self):
        return f"Investment(name={self.name}, principal={self.principal}, rate={self.rate})"

# PaymentMethod Class
class PaymentMethod(Notification):
    def __init__(self):
        super().__init__()
        self.methods = []

    def add_method(self, method):
        self.methods.append(method)
        self.add_notification(f"Payment method '{method}' added.")

    def remove_method(self, method):
        if method in self.methods:
            self.methods.remove(method)
            self.add_notification(f"Payment method '{method}' removed.")
        else:
            self.add_notification(f"Error: Payment method '{method}' not found.")

    def __repr__(self):
        return f"PaymentMethod(methods={self.methods})"

# RecurringExpense Class
class RecurringExpense(Notification):
    def __init__(self, name, amount, interval):
        super().__init__()
        self.name = name
        self.amount = amount
        self.interval = interval
        self.add_notification(f"Recurring expense '{name}' created for {amount} every {interval}.")

    def update_amount(self, amount):
        self.amount = amount
        self.add_notification(f"Recurring expense '{self.name}' updated to {amount}.")

    def __repr__(self):
        return f"RecurringExpense(name={self.name}, amount={self.amount}, interval={self.interval})"

# TaxCalculator Class
class TaxCalculator(Notification):
    def __init__(self, tax_rate):
        super().__init__()
        self.tax_rate = tax_rate

    def calculate_tax(self, amount):
        if amount < 0:
            self.add_notification("Error: Tax calculation failed. Negative amount provided.")
            raise ValueError("Amount cannot be negative")
        tax = amount * self.tax_rate / 100
        self.add_notification(f"Tax calculated: {tax} for amount {amount}.")
        return tax

    def __repr__(self):
        return f"TaxCalculator(tax_rate={self.tax_rate}%)"

# Transaction Class
class Transaction(Notification):
    def __init__(self, amount, category, description=None):
        super().__init__()
        self.amount = amount
        self.category = category
        self.description = description
        self.add_notification(f"Transaction created: {amount} in category '{category}'.")

    def __repr__(self):
        return f"Transaction(amount={self.amount}, category='{self.category}', description='{self.description}')"
