# Question 32:
# Define a structure "employee" with the following specifications.
# empno : integer
# ename : 20 characters
# basic, hra, da : float
# calculate() : a function to compute net pay as basic+hra+da with float return type.
# getdata() : a function to read values for empno, ename, basic, hra, da.
# dispdata() : a function to display all the data on the screen
# Write a main program to test the program.

class Employee:
    def __init__(self):
        self.empno = 0
        self.ename = ""
        self.basic = 0.0
        self.hra = 0.0
        self.da = 0.0
    
    def calculate(self):
        return self.basic + self.hra + self.da
    
    def getdata(self):
        self.empno = int(input("Enter Employee No: "))
        self.ename = input("Enter Employee Name: ")
        self.basic = float(input("Enter Basic Salary: "))
        self.hra = float(input("Enter HRA: "))
        self.da = float(input("Enter DA: "))
    
    def dispdata(self):
        print(f"Employee No: {self.empno}")
        print(f"Employee Name: {self.ename}")
        print(f"Basic: {self.basic}")
        print(f"HRA: {self.hra}")
        print(f"DA: {self.da}")
        print(f"Net Pay: {self.calculate()}")

# Main program
e = Employee()
e.getdata()
e.dispdata()
