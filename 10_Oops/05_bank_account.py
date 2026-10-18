from datetime import datetime


class Account:

    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def verify_pin(self):
        pin = input("Enter your PIN: ")
        return pin == "1213"

    def record_transaction(self, message):
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.history.append(f"[{timestamp}] {message}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
        except ValueError:
            print("Please enter a valid number!")
            return

        if amount <= 0:
            print("Please enter a valid positive amount!")
            return

        if not self.verify_pin():
            print("Incorrect PIN. Please try again!")
            return

        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully!")
        self.record_transaction(f"Deposited ₹{amount:.2f}")

    def withdraw(self):
        if not self.verify_pin():
            print("Incorrect PIN. Please try again!")
            return

        try:
            amount = float(input("Enter amount to withdraw: ₹"))
        except ValueError:
            print("Please enter a valid number!")
            return

        if amount <= 0:
            print("Please enter a valid positive amount!")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully!")
        self.record_transaction(f"Withdraw ₹{amount:.2f}")

    def check_balance(self):
        if not self.verify_pin():
            print("Incorrect PIN. Please try again!")
            return

        print(f"Current balance: ₹{self.balance:.2f}")

    def show_history(self):
        if not self.verify_pin():
            print("Incorrect PIN. Please try again!")
            return

        if not self.history:
            print("No transactions yet.")
            return

        print("\n===== TRANSACTION HISTORY =====")
        for number, transaction in enumerate(self.history, start=1):
            print(f"{number}. {transaction}")


def main():
    account = Account()

    while True:
        print("\n===== BANK ACCOUNT MENU =====")
        print("01. Deposit money")
        print("02. Withdraw money")
        print("03. Check balance")
        print("04. Show transaction history")
        print("05. Exit")

        choice = input("Enter your choice: ").lower().strip()

        if choice in ["01", "1", "deposit", "deposit money"]:
            account.deposit()

        elif choice in ["02", "2", "withdraw", "withdraw money"]:
            account.withdraw()

        elif choice in ["03", "3", "check", "balance", "check balance"]:
            account.check_balance()

        elif choice in ["04", "4", "history", "transaction history"]:
            account.show_history()

        elif choice in ["05", "5", "exit"]:
            print("Thank you for using our bank system!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
