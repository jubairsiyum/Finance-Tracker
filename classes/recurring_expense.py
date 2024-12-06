# Siyum's Code:

class RecurringExpense:
    def __init__(self, amount, frequency):
        self.amount = amount
        self.frequency = frequency

    def schedule(self):
        return f"Scheduled {self.amount} to repeat {self.frequency}"

    def cancel(self):
        return "Recurring expense cancelled"
