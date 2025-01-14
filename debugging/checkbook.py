class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook balance if funds are sufficient.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            amount = input("Enter the amount to deposit: $").strip()
            try:
                # Remove any non-numeric characters (like `$`) before conversion
                amount = float(amount.replace("$", ""))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif action == 'withdraw':
            amount = input("Enter the amount to withdraw: $").strip()
            try:
                # Remove any non-numeric characters (like `$`) before conversion
                amount = float(amount.replace("$", ""))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
