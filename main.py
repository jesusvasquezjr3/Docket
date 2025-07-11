import tkinter as tk
from gui import TaskGUI
from task_manager import TaskManager
from config import WINDOW_SIZE

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Docket - Task Manager")
    root.geometry(WINDOW_SIZE)
    root.configure(bg="#483f89")

    task_manager = TaskManager()
    app = TaskGUI(root, task_manager)
    root.mainloop()
