import pandas as pd
from datetime import datetime

class TaskManagerAgent:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, due_date):
        task = {
            'task_name': task_name,
            'due_date': pd.to_datetime(due_date),
            'status': 'Pending'
        }
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks

    def assign_task(self, task_name, agent):
        task = next((task for task in self.tasks if task['task_name'] == task_name), None)
        if task and task['status'] == 'Pending':
            agent.execute_task(task)
            task['status'] = 'In Progress'
        else:
            print(f"Task '{task_name}' is either completed or does not exist.")
