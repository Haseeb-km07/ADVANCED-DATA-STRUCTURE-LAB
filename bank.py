
class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("Updated Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Updated Balance:", self.balance)


acc_no = input("Enter Account Number: ")
name = input("Enter Name: ")
acc_type = input("Enter Account Type: ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(acc_no, name, acc_type, balance)

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)