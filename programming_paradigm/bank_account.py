# bank_account.py

class BankAccount:
    """A simple BankAccount class to handle deposits, withdrawals, and balance display."""

    def __init__(self, initial_balance=0.0):
        """Initialize account with an optional starting balance."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw an amount if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
