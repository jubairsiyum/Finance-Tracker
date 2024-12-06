# Siyum's Code

class Category:
    def __init__(self, name, budget_limit=0.0):
        self.name = name
        self.budget_limit = budget_limit

    def get_name(self):
        return self.name

    def set_budget_limit(self, limit):
        self.budget_limit = limit
