import tkinter as tk
from tkinter import messagebox


class BudgetPlannerApp:
    def __init__(self, master):
        self.master = master
        master.title("Budget Planner")

        self.budget = 0
        self.expenses = []

        # Create a label and entry for entering the budget
        self.budget_label = tk.Label(master, text="Enter your budget:")
        self.budget_label.pack(pady=5)

        self.budget_entry = tk.Entry(master)
        self.budget_entry.pack(pady=5)

        # Create a button to set the budget
        self.set_budget_button = tk.Button(
            master, text="Set Budget", command=self.set_budget)
        self.set_budget_button.pack(pady=5)

        # Create a label and entry for entering an expense
        self.expense_label = tk.Label(master, text="Enter an expense:")
        self.expense_label.pack(pady=5)

        self.expense_entry = tk.Entry(master)
        self.expense_entry.pack(pady=5)

        # Create a button to add the expense
        self.add_expense_button = tk.Button(
            master, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(pady=5)

        # Create a button to show the budget summary
        self.summary_button = tk.Button(
            master, text="Show Summary", command=self.show_summary)
        self.summary_button.pack(pady=5)

    def set_budget(self):
        try:
            # Get the budget value from the entry and convert it to a float
            self.budget = float(self.budget_entry.get())
            # Show a message box with the budget value
            messagebox.showinfo(
                "Budget Set", f"Budget set to: ${self.budget:.2f}")
        except ValueError:
            # Show an error message if the input is not a valid number
            messagebox.showerror(
                "Input Error", "Please enter a valid number for the budget.")

    def add_expense(self):
        try:
            # Get the expense value from the entry and convert it to a float
            expense = float(self.expense_entry.get())
            # Add the expense to the expenses list
            self.expenses.append(expense)
            # Show a message box with the added expense value
            messagebox.showinfo(
                "Expense Added", f"Expense added: ${expense:.2f}")
        except ValueError:
            # Show an error message if the input is not a valid number
            messagebox.showerror(
                "Input Error", "Please enter a valid number for the expense.")

    def show_summary(self):
        # Calculate the total expenses and remaining budget
        total_expenses = sum(self.expenses)
        remaining_budget = self.budget - total_expenses
        # Create a summary string with the budget, total expenses, and remaining budget
        summary = f"Budget: ${self.budget:.2f}\nTotal Expenses: ${
            total_expenses:.2f}\nRemaining Budget: ${remaining_budget:.2f}"
        # Show a message box with the budget summary
        messagebox.showinfo("Budget Summary", summary)


if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()
    # Create an instance of the BudgetPlannerApp class
    app = BudgetPlannerApp(root)
    # Start the Tkinter event loop
    root.mainloop()
