# Mahir's Code

class GoalReward:
    def __init__(self, goal_amount=0, reward=None):
        self.goal_amount = goal_amount
        self.reward = reward

    def set_goal(self, amount):
        self.goal_amount = amount

    def track_progress(self, current_amount):
        return current_amount >= self.goal_amount
