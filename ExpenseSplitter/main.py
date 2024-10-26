class ExpenseSplitter:
	def __init__(self):
		self.people = {}  # Dictionary to store people and their expenses
		self.total_expenses = 0  # Total expenses

	def add_person(self, name):
		if name not in self.people:
			self.people[name] = 0  # Initialize the person's expense to 0

	def add_expense(self, name, amount):
		if name in self.people:
			self.people[name] += amount  # Add the expense to the person's total
			self.total_expenses += amount  # Update the total expenses
		else:
			print(f"{name} is not in the list of people.")

	def calculate_splits(self):
		if not self.people:
			print("No people added.")
			return

		average_expense = self.total_expenses / len(self.people)  # Calculate the average expense per person
		balances = {name: amount - average_expense for name, amount in self.people.items()}  # Calculate the balance for each person

		for name, balance in balances.items():
			if balance > 0:
				print(f"{name} is owed ${balance:.2f}")
			elif balance < 0:
				print(f"{name} owes ${-balance:.2f}")
			else:
				print(f"{name} is settled.")

def main():
	splitter = ExpenseSplitter()

	while True:
		print("\nExpense Splitter Menu:")
		print("1. Add Person")
		print("2. Add Expense")
		print("3. Calculate Splits")
		print("4. Exit")

		choice = input("Enter your choice: ")

		if choice == '1':
			name = input("Enter the name of the person: ")
			splitter.add_person(name)  # Call the add_person method
		elif choice == '2':
			name = input("Enter the name of the person who paid: ")
			amount = float(input("Enter the amount paid: "))
			splitter.add_expense(name, amount)  # Call the add_expense method
		elif choice == '3':
			splitter.calculate_splits()  # Call the calculate_splits method
		elif choice == '4':
			break
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()