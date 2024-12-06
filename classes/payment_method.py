# Shakib's Code

class PaymentMethod:
    def __init__(self):
        self.methods = []  # Initialize the methods list to store payment methods

    def add_method(self, method):
        """Add a new payment method to the list."""
        self.methods.append(method)
        print(f"{method.name} has been added to the payment methods list.")

    def remove_method(self, method):
        """Remove a payment method from the list."""
        if method in self.methods:
            self.methods.remove(method)
            print(f"{method.name} has been removed from the payment methods list.")
        else:
            print(f"{method.name} not found in the payment methods list.")

    def list_methods(self):
        """List all payment methods in the methods list."""
        if not self.methods:
            print("No payment methods available.")
        else:
            for method in self.methods:
                print(f"Name: {method.name}, Description: {method.description}, Active: {method.is_active}")

    def __repr__(self):
        """Representation of PaymentMethod class for easy viewing."""
        return f"PaymentMethod(name={self.name}, description={self.description}, is_active={self.is_active})"

class PaymentMethodDetails:
    def __init__(self, name, description):
        self.name = name  # Name of the payment method (e.g., Cash, Credit Card)
        self.description = description  # Description of the payment method
        self.is_active = True  # Payment method status (active or inactive)

    def deactivate(self):
        """Deactivate this payment method."""
        self.is_active = False
        print(f"{self.name} payment method has been deactivated.")
    
    def activate(self):
        """Activate this payment method."""
        self.is_active = True
        print(f"{self.name} payment method is now active.")
    
    def update_description(self, new_description):
        """Update the description of the payment method."""
        self.description = new_description
        print(f"Description for {self.name} updated to: {self.description}")

    def get_method_details(self):
        """Return the payment method details as a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active
        }
