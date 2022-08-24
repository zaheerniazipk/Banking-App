# Project: Bank Application

class Bank:

    # Dunder Method | Magic Method
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transactions_log(f"Deposited amount Rs.{amount}")

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.transactions_log(f"Withdrew amount Rs.{amount}")

    def transactions_log(self, transaction_string):
        # Context Manager
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\tBalance: {self.balance}\n")

        file.close()


# Object instantiation
account = Bank(1000.00)

while True:
    print("""\nOption Menu:
****************************
    1. Deposit an amount
    2. Withdraw an amount
    3. Account Balance
    4. Leaving the ATM
****************************
    """)
    options = ["1", "2", "3", "4"]

    try:
        action = input("Your Choice: ")
    except KeyboardInterrupt:
        print("\nLeaving the ATM\n")
        exit()

    except NameError:
        print("Sorry,action not defined!")
        break

    if action in options:
        if action == "1":
            amount = input("How much amount, do you want to deposit: ")
            account.deposit(amount)
        elif action == "2":
            amount = input("How much amount, do you want to withdraw: ")
            account.withdraw(amount)

        elif action == "3":
            pass
            # print("Your balance: ", account.balance)

        elif action == "4":
            print("\nLeaving the ATM\n")
            exit()

        print("Your balance: ", account.balance)

    else:
        print("That is not a valid action, try again!")
        continue
