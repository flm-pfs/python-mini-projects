class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to account {
                  self.account_number}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {
                  self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Holder: {self.account_holder}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        if account_number not in self.accounts:
            new_account = Account(
                account_number, account_holder, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account {account_number} created for {
                  account_holder} with initial balance {initial_balance}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None

    def list_accounts(self):
        for account in self.accounts.values():
            print(account)


def main():
    bank = Bank()

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. List Accounts")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(
                account_number, account_holder, initial_balance)
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
        elif choice == '4':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Balance: {account.get_balance()}")
        elif choice == '5':
            bank.list_accounts()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
