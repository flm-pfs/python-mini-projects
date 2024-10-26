import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")

        self.tasks = []  # List to store the tasks

        # Create a frame to hold the task entry and add button
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Create an entry widget for the user to enter tasks
        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        # Create a button to add tasks
        self.add_button = tk.Button(
            self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Create a listbox to display the tasks
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=15)
        self.tasks_listbox.pack(pady=10)

        # Create a button to remove tasks
        self.remove_button = tk.Button(
            self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        # Create a button to clear all tasks
        self.clear_button = tk.Button(
            self.root, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack()

    def add_task(self):
        # Get the task from the task entry widget
        task = self.task_entry.get()
        if task:
            # Add the task to the tasks list
            self.tasks.append(task)
            # Insert the task into the tasks listbox
            self.tasks_listbox.insert(tk.END, task)
            # Clear the task entry widget
            self.task_entry.delete(0, tk.END)
        else:
            # Show a warning message if no task is entered
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            # Get the index of the selected task in the listbox
            selected_index = self.tasks_listbox.curselection()[0]
            # Remove the task from the tasks list
            del self.tasks[selected_index]
            # Remove the task from the tasks listbox
            self.tasks_listbox.delete(selected_index)
        except IndexError:
            # Show a warning message if no task is selected
            messagebox.showwarning(
                "Warning", "You must select a task to remove.")

    def clear_tasks(self):
        # Clear all tasks from the tasks list and listbox
        self.tasks.clear()
        self.tasks_listbox.delete(0, tk.END)


if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()
    # Create an instance of the TodoApp class
    app = TodoApp(root)
    # Start the Tkinter event loop
    root.mainloop()
