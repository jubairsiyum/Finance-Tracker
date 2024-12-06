# Siyum's Code

class GoalReward:
    def __init__(self, goal_amount, reward):
        self.goal_amount = goal_amount
        self.reward = reward

    def set_goal(self, amount):
        self.goal_amount = amount

    def track_progress(self, current_amount):
        return current_amount >= self.goal_amount
