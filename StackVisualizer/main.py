import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack items

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top item from the stack
        else:
            # Raise an error if the stack is empty
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            # Return the top item from the stack without removing it
            return self.items[-1]
        else:
            # Raise an error if the stack is empty
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)  # Return the number of items in the stack


class StackVisualizationApp:
    def __init__(self, root):
        self.stack = Stack()  # Create an instance of the Stack class
        self.root = root
        self.root.title("Stack Visualization")

        # Create a frame to display the stack
        self.stack_frame = tk.Frame(self.root)
        self.stack_frame.pack(pady=20)

        self.stack_labels = []  # List to store the labels representing stack items
        self.update_stack_visualization()  # Update the stack visualization

        # Create a frame for controls
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(pady=20)

        # Create an entry widget for user input
        self.entry = tk.Entry(self.controls_frame, width=10)
        self.entry.grid(row=0, column=0, padx=5)

        self.push_button = tk.Button(
            # Create a button to push an item to the stack
            self.controls_frame, text="Push", command=self.push_item)
        self.push_button.grid(row=0, column=1, padx=5)

        self.pop_button = tk.Button(
            # Create a button to pop an item from the stack
            self.controls_frame, text="Pop", command=self.pop_item)
        self.pop_button.grid(row=0, column=2, padx=5)

        self.peek_button = tk.Button(
            # Create a button to peek at the top item of the stack
            self.controls_frame, text="Peek", command=self.peek_item)
        self.peek_button.grid(row=0, column=3, padx=5)

    def update_stack_visualization(self):
        for label in self.stack_labels:
            label.destroy()  # Remove existing labels from the stack frame
        self.stack_labels = []
        for item in reversed(self.stack.items):
            label = tk.Label(self.stack_frame, text=str(
                # Create a label for each stack item
                item), borderwidth=1, relief="solid", width=10, height=2)
            label.pack(side="top")
            # Add the label to the stack_labels list
            self.stack_labels.append(label)

    def push_item(self):
        item = self.entry.get()  # Get the item from the entry widget
        if item:
            self.stack.push(item)  # Push the item to the stack
            self.update_stack_visualization()  # Update the stack visualization
            self.entry.delete(0, tk.END)  # Clear the entry widget
        else:
            messagebox.showwarning(
                # Show a warning message if no item is entered
                "Input Error", "Please enter an item to push.")

    def pop_item(self):
        try:
            item = self.stack.pop()  # Pop an item from the stack
            self.update_stack_visualization()  # Update the stack visualization
            # Show a message with the popped item
            messagebox.showinfo("Popped Item", f"Popped item: {item}")
        except IndexError:
            # Show a warning message if the stack is empty
            messagebox.showwarning("Stack Error", "Stack is empty.")

    def peek_item(self):
        try:
            item = self.stack.peek()  # Peek at the top item of the stack
            # Show a message with the top item
            messagebox.showinfo("Peeked Item", f"Top item: {item}")
        except IndexError:
            # Show a warning message if the stack is empty
            messagebox.showwarning("Stack Error", "Stack is empty.")


if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    # Create an instance of the StackVisualizationApp class
    app = StackVisualizationApp(root)
    root.mainloop()  # Start the main event loop
