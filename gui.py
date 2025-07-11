import tkinter as tk
from tkinter import ttk
from config import COLORS, WINDOW_SIZE, ICON_PATH

class TaskGUI:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.setup_gui()

    def setup_gui(self):
        # Main frame with glass effect simulation
        main_frame = tk.Canvas(self.root, bg=COLORS["panel_border"], highlightthickness=0)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Configure Treeview style for alternating colors, row height, and black text
        style = ttk.Style()
        style.configure("Treeview",
                        rowheight=30,  # Increase row height for wider rows
                        background=COLORS["panel_border"],
                        foreground="#000000",  # Set text color to black
                        fieldbackground=COLORS["panel_border"])
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.map("Treeview", background=[("selected", COLORS["circles"])])

        # Task list
        self.task_tree = ttk.Treeview(main_frame, columns=("Task", "Status"), show="headings", style="Treeview")
        self.task_tree.heading("Task", text="Task")
        self.task_tree.heading("Status", text="Status")
        self.task_tree.column("Task", width=300)
        self.task_tree.column("Status", width=100, anchor="center")  # Center the Status column
        self.task_tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Tag configuration for alternating row colors
        self.task_tree.tag_configure("evenrow", background="#D5E8FF")  # Lighter shade for even rows
        self.task_tree.tag_configure("oddrow", background=COLORS["panel_border"])  # Default for odd rows

        # Input frame
        input_frame = tk.Frame(main_frame, bg=COLORS["circles"])
        input_frame.pack(pady=10, fill="x")

        self.task_entry = ttk.Entry(input_frame)
        self.task_entry.pack(side="left", padx=5, fill="x", expand=True)

        add_button = ttk.Button(input_frame, text="Add", command=self.add_task)
        add_button.pack(side="left", padx=5)

        delete_button = ttk.Button(input_frame, text="Delete", command=self.delete_task)
        delete_button.pack(side="left", padx=5)

        toggle_button = ttk.Button(input_frame, text="Toggle", command=self.toggle_task)
        toggle_button.pack(side="left", padx=5)

        # Load initial tasks
        self.update_task_list()

        # Make responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Set window icon
        self.root.iconphoto(True, tk.PhotoImage(file=ICON_PATH))

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_manager.add_task(task_text)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()

    def delete_task(self):
        selected = self.task_tree.selection()
        if selected:
            index = self.task_tree.index(selected[0])
            self.task_manager.delete_task(index)
            self.update_task_list()

    def toggle_task(self):
        selected = self.task_tree.selection()
        if selected:
            index = self.task_tree.index(selected[0])
            self.task_manager.toggle_task(index)
            self.update_task_list()

    def update_task_list(self):
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
        for i, task in enumerate(self.task_manager.get_tasks()):
            status = "✅" if task["completed"] else "⏳"
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.task_tree.insert("", "end", iid=i, values=(task["text"], status), tags=(tag,))
