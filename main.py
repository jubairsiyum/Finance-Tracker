# Merge all classes, create objects, previewing the final result
import numpy as np
from classes.user import User
from classes.finance_tracker import FinanceTracker
from classes.transaction import Transaction, TransactionManager
from classes.category import Category
from classes.currency_converter import CurrencyConverter
from classes.notification_system import NotificationSystem
from classes.payment_method import PaymentMethod, PaymentMethodDetails
from classes.recurring_expense import RecurringExpense
from classes.tax_calculator import TaxCalculator
from classes.investment import Investment
from classes.goal_reward import GoalReward


def main():
    global message
    print("Welcome to the Finance Tracker!")

    # User Registration/Login
    print("\nLet's start by creating your user account:")
    name = input("Enter your name: ")
    income = float(input("Enter your monthly income: "))
    currency = input("Enter your preferred currency (e.g., USD, EUR, GBP): ")
    password = input("Set your account password: ")

    # Create User object
    user = User(name, income, currency, password)
    print(f"\nAccount created successfully for {user.get_name()}!")

    # Initialize other objects
    finance_tracker = FinanceTracker(user)
    transaction_manager = TransactionManager()
    converter = CurrencyConverter()
    notification_system = NotificationSystem("Welcome!", user.get_name())
    payment_method = PaymentMethod()
    tax_calculator = TaxCalculator(tax_rate=0.15)  # Example tax rate
    goal_reward = GoalReward(goal_amount=0, reward=None)
    investments = []
    recurring_expenses = []

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a Transaction")
        print("2. View Transactions")
        print("3. Manage Categories")
        print("4. Set a Financial Goal")
        print("5. Track Goal Progress")
        print("6. Add a Recurring Expense")
        print("7. View Investments")
        print("8. Calculate Tax")
        print("9. Convert Currency")
        print("10. Notifications")
        print("11. Payment Methods")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a transaction
            amount = float(input("Enter transaction amount: "))
            category_name = input("Enter transaction category: ")
            date = input("Enter transaction date (YYYY-MM-DD): ")

            # Check if category exists or create one
            category = next((cat for cat in finance_tracker.categories if cat.get_name() == category_name), None)
            if not category:
                budget_limit = float(input(f"Set a budget limit for the new category '{category_name}': "))
                category = Category(category_name, budget_limit)
                finance_tracker.categories.append(category)

            # Using NumPy for handling transaction data in array
            transaction = Transaction(amount, category_name, date)
            finance_tracker.add_transaction(transaction)
            print("Transaction added successfully!")

        elif choice == "2":
            # View all transactions
            print("\n--- Transactions ---")
            transactions_array = np.array(
                [(txn.get_amount(), txn.category, txn.date) for txn in finance_tracker.transactions])
            for txn in transactions_array:
                print(f"Amount: {txn[0]} | Category: {txn[1]} | Date: {txn[2]}")
        

        elif choice == "3":
            # Manage categories
            print("\n--- Categories ---")
            categories_array = np.array([(cat.get_name(), cat.budget_limit) for cat in finance_tracker.categories])
            for cat in categories_array:
                print(f"Category: {cat[0]} | Budget Limit: {cat[1]}")
            modify = input("Would you like to modify a category? (yes/no): ")
            if modify.lower() == 'yes':
                category_name = input("Enter the category name to modify: ")
                category = next((cat for cat in finance_tracker.categories if cat.get_name() == category_name), None)
                if category:
                    new_budget = float(input("Enter the new budget limit: "))
                    category.set_budget_limit(new_budget)
                    print("Budget limit updated successfully!")
                else:
                    print("Category not found.")

        elif choice == "4":
            # Set a financial goal
            goal_amount = float(input("Enter your financial goal amount: "))
            goal_reward.set_goal(goal_amount)
            print(f"Financial goal of {goal_amount} set successfully!")

        elif choice == "5":
            # Track goal progress
            print("\n--- Goal Progress ---")
            progress = goal_reward.track_progress(finance_tracker.get_total_expenses())
            print(f"Goal Progress: {progress:.2f}%")

        elif choice == "6":
            # Add a recurring expense
            print("\n--- Recurring Expense ---")
            amount = float(input("Enter the recurring expense amount: "))
            frequency = input("Enter the frequency (e.g., monthly, yearly): ")
            expense = RecurringExpense(amount, frequency)
            recurring_expenses.append(expense)
            print("Recurring expense added successfully!")

        elif choice == "7":
            # View investments
            print("\n--- Investments ---")
            for invest in investments:
                print(f"Amount: {invest.amount} | Returns: {invest.returns}")
            add_investment = input("Would you like to add an investment? (yes/no): ")
            if add_investment.lower() == 'yes':
                amount = float(input("Enter investment amount: "))
                returns = float(input("Enter expected returns: "))
                investment = Investment(amount, returns)
                investments.append(investment)
                print("Investment added successfully!")

        elif choice == "8":
            # Calculate tax
            print("\n--- Tax Calculator ---")
            total_tax = tax_calculator.calculate_tax(finance_tracker.get_total_expenses())
            print(f"Total Tax: {total_tax:.2f}")

        elif choice == "9":
            # Convert currency
            amount = float(input("Enter amount to convert: "))
            from_currency = input("Enter source currency: ")
            to_currency = input("Enter target currency: ")
            try:
                converted_amount = converter.static_convert(amount, from_currency, to_currency)
                print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "10":
            # Notifications
            print("\n--- Notifications ---")
            if notification_system.notifications:
                for notification in notification_system.notifications:
                    print(notification)
            else:
                print("No notifications available.")

            notify = input("Add a notification? (yes/no): ")
            if notify.lower() == 'yes':
                message = input("Enter the notification message: ")
            notification_system.set_notification(message)
            print("Notification added successfully!")


        elif choice == "11":

            # Payment methods

            print("\n--- Payment Methods ---")

            if not payment_method.methods:

                print("No payment methods available.")

            else:

                print("Available payment methods:")

                for method in payment_method.methods:
                    print(f"- {method.name} (Description: {method.description}, Active: {method.is_active})")

            add_method = input("Add a payment method? (yes/no): ").strip().lower()

            if add_method == 'yes':

                method_name = input("Enter payment method name: ").strip()

                method_description = input("Enter payment method description: ").strip()

                # Create a PaymentMethodDetails object

                new_method = PaymentMethodDetails(name=method_name, description=method_description)

                payment_method.add_method(new_method)

                print(f"Payment method '{method_name}' added successfully!")

            else:

                print("Returning to the main menu.")


        elif choice == "12":
            print("Exiting the Finance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
