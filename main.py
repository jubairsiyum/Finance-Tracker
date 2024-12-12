import json
from datetime import datetime, timedelta

class Authentication:
    FILE_PATH = "users.json"

    @staticmethod
    def load_users():
        try:
            with open(Authentication.FILE_PATH, "r") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
                else:
                    raise ValueError("Invalid data format")
        except (FileNotFoundError, ValueError):
            return {}

    @staticmethod
    def save_users(users):
        with open(Authentication.FILE_PATH, "w") as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def is_valid_username(username):
        return len(username) > 3 and username.isalnum()

    @staticmethod
    def is_valid_password(password):
        return len(password) > 5  # Example validation: Minimum length

    @staticmethod
    def register(username, password):
        if not Authentication.is_valid_username(username):
            print("Invalid username. It must be alphanumeric and at least 4 characters.")
            return False
        if not Authentication.is_valid_password(password):
            print("Invalid password. It must be at least 6 characters.")
            return False

        users = Authentication.load_users()
        if username in users:
            print("Username already exists.")
            return False
        users[username] = password
        Authentication.save_users(users)
        print("Registration successful.")
        return True

    @staticmethod
    def login(username, password):
        users = Authentication.load_users()
        if users.get(username) == password:
            print("Login successful.")
            return True
        print("Invalid username or password.")
        return False


# Main Application
class FinanceApp:
    TRANSACTION_FILE = "transactions.json"
    def __init__(self, username):
        self.username = username
        self.transactions = self.load_data(self.TRANSACTION_FILE).get(username, [])
        self.categories = {}
        self.financial_goal = None
        self.recurring_expenses = []
        self.investments = []
        self.notifications = []
        self.payment_methods = []

        if not self.load_data(self.TRANSACTION_FILE):
            self.save_data(self.TRANSACTION_FILE, {})

    def save_data(self, file_name, data):
        try:
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data to {file_name}: {e}")

    def load_data(self, file_name):
        try:
            with open(file_name, "r") as file:
                data = file.read().strip()
                return json.load(file) if data else{}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    def save_transactions(self):
        data = self.load_data(self.TRANSACTION_FILE)
        data[self.username] = self.transactions
        self.save_data(self.TRANSACTION_FILE, data)

    def add_transaction(self, amount, category, description):
        if category not in self.categories:
            self.categories[category] = []  # Add category if not present
            self.add_notification(f"Category '{category}' automatically added via transaction.")
    
        transaction = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
        self.transactions.append(transaction)
        self.save_transactions()
        self.add_notification(f"Transaction added: {description} for {amount} in {category}")
        print("Transaction added.")



    def view_transactions(self):
        print("\nTransactions:")
        if not self.transactions:
            print("No transactions found.")
            return
        for i, transaction in enumerate(self.transactions, 1):
            print(f"{i}. Amount: {transaction['amount']} | Category: {transaction['category']} | "
              f"Description: {transaction['description']} | Date: {transaction['date']}")


    def manage_categories(self, action, category_name):
        if action == "add":
            self.categories[category_name] = []
            self.add_notification(f"Category '{category_name}' added.")
            print(f"Category '{category_name}' added.")
        elif action == "delete" and category_name in self.categories:
            del self.categories[category_name]
            self.add_notification(f"Category '{category_name}' deleted.")
            print(f"Category '{category_name}' deleted.")
        else:
            print("Invalid action or category not found.")

    def set_financial_goal(self, amount):
        self.financial_goal = {
            "goal": amount,
            "progress": 0
        }
        self.add_notification(f"Financial goal of {amount} set.")
        print(f"Financial goal of {amount} set.")

    def track_goal_progress(self):
        if not self.financial_goal:
            print("No financial goal set.")
            return

        progress = sum(t["amount"] for t in self.transactions if t["amount"] > 0)
        self.financial_goal["progress"] = progress
        print(f"Goal: {self.financial_goal['goal']}, Progress: {self.financial_goal['progress']}")
        if progress >= self.financial_goal["goal"]:
            print("Warning! You've reached your financial goal!")


    def add_recurring_expense(self, amount, interval, description):
        expense = {
            "amount": amount,
            "interval": interval,
            "description": description,
            "next_due": (datetime.now() + timedelta(days=interval)).strftime('%Y-%m-%d')
        }
        self.recurring_expenses.append(expense)
        self.add_notification(f"Recurring expense added: {description} for {amount} every {interval} days.")
        print("Recurring expense added.")

    def view_recurring_expenses(self):
        print("\nRecurring Expenses:")
        for expense in self.recurring_expenses:
            print(expense)

    def add_investment(self, amount, description):
        investment = {
            "amount": amount,
            "description": description,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.investments.append(investment)
        self.add_notification(f"Investment added: {description} for {amount}.")
        print("Investment added.")

    def view_investments(self):
        print("\nInvestments:")
        if not self.investments:
            print("No investments recorded.")
            return
        for i, investment in enumerate(self.investments, 1):
            print(f"{i}. Amount: {investment['amount']} | Description: {investment['description']} | "
              f"Date: {investment['date']}")


    def calculate_tax(self, income):
        if income <= 300000:
            tax = 0
        elif income <= 700000:
            tax = (income - 300000) * 0.1
        elif income <= 3000000:
            tax = 40000 + (income - 700000) * 0.15
        else:
            tax = 40000 + 345000 + (income - 3000000) * 0.25
        self.add_notification(f"Tax calculated for income {income}: {tax}")
        print(f"Calculated tax: {tax}")
        return tax

    def convert_currency(self, amount, to_currency):
        rates = {"USD": 95, "EUR": 110, "INR": 1.3}
        if to_currency in rates:
            converted = amount / rates[to_currency]
            self.add_notification(f"Converted {amount} BDT to {converted:.2f} {to_currency}.")
            print(f"{amount} BDT is {converted:.2f} {to_currency}.")
            return converted
        print("Currency not supported.")
        return None

    def add_notification(self, message):
        notification = {
            "message": message,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.notifications.append(notification)

    def view_notifications(self):
        print("\nNotifications:")
        if not self.notifications:
            print("No notifications available.")
            return
        for i, notification in enumerate(self.notifications, 1):
            print(f"{i}. {notification['message']} (Date: {notification['date']})")


    def add_payment_method(self, method):
        self.payment_methods.append(method)
        self.add_notification(f"Payment method '{method}' added.")
        print(f"Payment method '{method}' added.")

    def view_payment_methods(self):
        print("\nPayment Methods:")
        for method in self.payment_methods:
            print(method)


    def display_cse222_art():
        print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌          ▐░▌                         ▐░▌          ▐░▌          ▐░▌
▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄                ▐░▌          ▐░▌          ▐░▌
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌      ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░▌           ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌                    ▐░▌▐░▌               ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
""")

    display_cse222_art()
        

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Add a Transaction")
            print("2. View Transactions")
            print("3. Manage Categories")
            print("4. Set a Financial Goal")
            print("5. Track Goal Progress")
            print("6. Add a Recurring Expense")
            print("7. View Recurring Expenses")
            print("8. Add an Investment")
            print("9. View Investments")
            print("10. Calculate Tax")
            print("11. Convert Currency")
            print("12. View Notifications")
            print("13. Add Payment Method")
            print("14. View Payment Methods")
            print("15. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                self.add_transaction(amount, category, description)
            elif choice == "2":
                self.view_transactions()
            elif choice == "3":
                action = input("Add or delete category? ")
                category_name = input("Enter category name: ")
                self.manage_categories(action, category_name)
            elif choice == "4":
                amount = float(input("Enter goal amount: "))
                self.set_financial_goal(amount)
            elif choice == "5":
                self.track_goal_progress()
            elif choice == "6":
                amount = float(input("Enter amount: "))
                interval = int(input("Enter interval in days: "))
                description = input("Enter description: ")
                self.add_recurring_expense(amount, interval, description)
            elif choice == "7":
                self.view_recurring_expenses()
            elif choice == "8":
                amount = float(input("Enter investment amount: "))
                description = input("Enter investment description: ")
                self.add_investment(amount, description)
            elif choice == "9":
                self.view_investments()
            elif choice == "10":
                income = float(input("Enter income: "))
                self.calculate_tax(income)
            elif choice == "11":
                amount = float(input("Enter amount in BDT: "))
                to_currency = input("Convert to (USD, EUR, INR): ")
                self.convert_currency(amount, to_currency)
            elif choice == "12":
                self.view_notifications()
            elif choice == "13":
                method = input("Enter payment method name: ")
                self.add_payment_method(method)
            elif choice == "14":
                self.view_payment_methods()
            elif choice == "15":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

def show_authentication_menu():
    print("\nAuthentication Menu:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if Authentication.login(username, password):
            return username
        else:
            print("Login failed. Please try again.")
            return None
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if Authentication.register(username, password):
            return username
        else:
            print("Registration failed. Please try again.")
            return None
    elif choice == "3":
        print("Exiting... Goodbye!")
        exit()
    else:
        print("Invalid choice. Please select again.")
        return None


if __name__ == "__main__":
    print("Welcome to Finance Manager")

    username = None
    while not username:
        username = show_authentication_menu()

    app = FinanceApp(username)
    app.main_menu()
