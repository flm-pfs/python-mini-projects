import json


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        # Create a dictionary to represent the expense
        expense = {
            "description": description,
            "amount": amount
        }
        # Add the expense to the list of expenses
        self.expenses.append(expense)
        print(f"Expense '{description}' added successfully.")

    def list_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            for expense in self.expenses:
                # Print the description and amount of each expense
                print(f"Description: {expense['description']}, Amount: ${
                      expense['amount']:.2f}")

    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            # Save the expenses list as JSON to the specified file
            json.dump(self.expenses, file)
        print(f"Expenses saved to {filename}.")

    def load_expenses(self, filename):
        try:
            with open(filename, 'r') as file:
                # Load the expenses from the specified file
                self.expenses = json.load(file)
            print(f"Expenses loaded from {filename}.")
        except FileNotFoundError:
            print("File not found.")

    def menu(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. List Expenses")
            print("3. Save Expenses")
            print("4. Load Expenses")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                description = input("Enter description: ")
                amount = float(input("Enter amount: "))
                self.add_expense(description, amount)
            elif choice == '2':
                self.list_expenses()
            elif choice == '3':
                filename = input("Enter filename to save: ")
                self.save_expenses(filename)
            elif choice == '4':
                filename = input("Enter filename to load: ")
                self.load_expenses(filename)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    expense_tracker.menu()
