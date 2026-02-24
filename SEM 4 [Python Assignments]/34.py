# Question 34:
# Create a class "Account" to represent the details of a bank account.
# accno : account number (integer)
# name : customer name (20 characters)
# balance : balance amount (float)
# deposit(amount) : member function to deposit amount
# withdraw(amount) : member function to withdraw amount
# getdata() : to read the data
# dispdata() : to display the data
# Write a main function to test the class.

class Account:
    def __init__(self):
        self.accno = 0
        self.name = ""
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")
    
    def getdata(self):
        self.accno = int(input("Enter Account No: "))
        self.name = input("Enter Name: ")
        self.balance = float(input("Enter Initial Balance: "))
    
    def dispdata(self):
        print(f"Account No: {self.accno}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

# Main program
acc = Account()
acc.getdata()
acc.dispdata()
acc.deposit(float(input("Enter amount to deposit: ")))
acc.withdraw(float(input("Enter amount to withdraw: ")))
acc.dispdata()
