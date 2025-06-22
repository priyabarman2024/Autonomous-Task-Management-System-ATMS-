import random

class DecisionMakingAgent:
    def __init__(self):
        self.task_priority = {}

    def evaluate_task(self, task):
        # Simulating decision making with random prioritization
        priority = random.choice(['High', 'Medium', 'Low'])
        self.task_priority[task['task_name']] = priority
        return priority
