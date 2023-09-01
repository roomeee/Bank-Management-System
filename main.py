from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, amount, timestamp):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.record_transaction("Deposit", amount)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.record_transaction("Withdrawal", -amount)
            return True
        return False

    def get_balance(self):
        return self.balance

    def record_transaction(self, transaction_type, amount):
        transaction = Transaction(transaction_type, amount, datetime.now())
        self.transactions.append(transaction)

    def get_transaction_history(self):
        return self.transactions

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def __str__(self):
        return super().__str__() + f"\nInterest Rate: {self.interest_rate}"


class BankManagementSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, account_type="basic", initial_balance=0):
        if account_number in self.accounts:
            print("An account with the same account number already exists.")
            return None
        if account_number not in self.accounts:
            if account_type == "savings":
                new_account = SavingsAccount(account_number, account_holder, initial_balance)
            else:
                new_account = BankAccount(account_number, account_holder, initial_balance)

            self.accounts[account_number] = new_account
            print("Account created successfully!")
            return new_account

        return None

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account and to_account:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                return True
        return False

    def get_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            return account.get_balance()
        return None

    def display_transaction_history(self, account_number):
        account = self.get_account(account_number)
        if account:
            transaction_history = account.get_transaction_history()
            for transaction in transaction_history:
                print(
                    f"Transaction Type: {transaction.transaction_type}\nAmount: {transaction.amount}\nTimestamp: {transaction.timestamp}\n"
                )

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} has been closed.")
        else:
            print(f"Account {account_number} not found.")

    def main_menu(self):
        while True:
            print("===== Bank Management System =====")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Balance")
            print("6. Display Transaction History")
            print("7. Close Account")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                account_type = input("Enter account type (basic/savings): ")
                account_number = input("Enter account number: ")
                account_holder = input("Enter account holder name: ")
                initial_balance = float(input("Enter initial balance: "))
                self.create_account(account_number, account_holder, account_type, initial_balance)

            elif choice == "2":
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount to deposit: "))
                if self.deposit(account_number, amount):
                    print("Deposit successful!")
                else:
                    print("Invalid account number or amount.")
            elif choice == "3":
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount to withdraw: "))
                if self.withdraw(account_number, amount):
                    print("Withdrawal successful!")
                else:
                    print("Invalid account number or insufficient balance.")
            elif choice == "4":
                from_account_number = input("Enter your account number: ")
                to_account_number = input("Enter recipient's account number: ")
                amount = float(input("Enter amount to transfer: "))
                if self.transfer(from_account_number, to_account_number, amount):
                    print("Transfer successful!")
                else:
                    print("Invalid account numbers or insufficient balance.")
            elif choice == "5":
                account_number = input("Enter account number: ")
                balance = self.get_balance(account_number)
                if balance is not None:
                    print(f"Current balance: {balance}")
                else:
                    print("Invalid account number.")
            elif choice == "6":
                account_number = input("Enter account number: ")
                self.display_transaction_history(account_number)
            elif choice == "7":
                account_number = input("Enter account number to close: ")
                self.close_account(account_number)
            elif choice == "8":
                print("Exiting Bank Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    bank_system = BankManagementSystem()
    bank_system.main_menu()
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"


class EBook(Book):
    def __init__(self, title, author, year, format_type):
        super().__init__(title, author, year)
        self.format_type = format_type

    def get_info(self):
        book_info = super().get_info()
        return f"{book_info}\nFormat: {self.format_type}"

    def is_available_online(self):
        return True


book1 = Book("Angels and demons", "Dan brown", 1995)
ebook1 = EBook("40 rules of love", "Elif", 2015, "PDF")

print("Book 1:")
print(book1.get_info())

print("\nEBook 1:")
print(ebook1.get_info())
print("Available online:", ebook1.is_available_online())

