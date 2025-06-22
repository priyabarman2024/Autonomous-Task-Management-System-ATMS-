class ExecutionAgent:
    def __init__(self):
        pass

    def execute_task(self, task):
        print(f"Executing task: {task['task_name']}")
        # Here, you would add code to execute the task like sending emails, etc.
        task['status'] = 'Completed'
        print(f"Task '{task['task_name']}' completed.")
