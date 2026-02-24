# Question 33:
# Define a structure "student" with the following specifications.
# rollno : integer
# name : 20 characters
# marks1, marks2, marks3 : float
# average() : a function that returns average of three marks
# getdata() : a function to read values for rollno, name, marks1, marks2, marks3.
# dispdata() : a function to display all the data on the screen
# Write a main program to test the program.

class Student:
    def __init__(self):
        self.rollno = 0
        self.name = ""
        self.marks1 = 0.0
        self.marks2 = 0.0
        self.marks3 = 0.0
    
    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3
    
    def getdata(self):
        self.rollno = int(input("Enter Roll No: "))
        self.name = input("Enter Name: ")
        self.marks1 = float(input("Enter Marks 1: "))
        self.marks2 = float(input("Enter Marks 2: "))
        self.marks3 = float(input("Enter Marks 3: "))
    
    def dispdata(self):
        print(f"Roll No: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Marks 1: {self.marks1}")
        print(f"Marks 2: {self.marks2}")
        print(f"Marks 3: {self.marks3}")
        print(f"Average: {self.average()}")

# Main program
s = Student()
s.getdata()
s.dispdata()
