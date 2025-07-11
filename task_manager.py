import json
import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task_text):
        self.tasks.append({"text": task_text, "completed": False})
        self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.save_tasks()

    def get_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
