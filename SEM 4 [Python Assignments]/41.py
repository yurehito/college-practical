# Question 41:
# Define a class student with the following specification:
# rollno : integer
# sname : 20 characters
# Derive two classes arst and scst. The class arst will represent students
# belonging to Arts stream and the class scst will represent students belonging
# to Science stream.
# The arst class will have additional data members ph, hs, en and as obtained by a student in Philosophy, History, English and Assamese.
# The class scst will have additional data members sph, ch, ma and en obtained in Physics, Chemistry, Mathematics and English.
# Write the following member functions in the classes arst and scst;
# ctotal() : a function to calculate the total marks obtained by a student
# takedata() : a function to accept values of the data members and store them
# a function to display the marks sheet of a student.

class Student:
    def __init__(self):
        self.rollno = 0
        self.sname = ""
    
    def getdata(self):
        self.rollno = int(input("Enter Roll No: "))
        self.sname = input("Enter Name: ")

class ArtsStudent(Student):
    def __init__(self):
        super().__init__()
        self.ph = 0.0
        self.hs = 0.0
        self.en = 0.0
        self.as_marks = 0.0
    
    def takedata(self):
        super().getdata()
        self.ph = float(input("Enter Philosophy marks: "))
        self.hs = float(input("Enter History marks: "))
        self.en = float(input("Enter English marks: "))
        self.as_marks = float(input("Enter Assamese marks: "))
    
    def ctotal(self):
        return self.ph + self.hs + self.en + self.as_marks
    
    def display(self):
        print(f"\n--- Arts Student ---")
        print(f"Roll No: {self.rollno}")
        print(f"Name: {self.sname}")
        print(f"Philosophy: {self.ph}")
        print(f"History: {self.hs}")
        print(f"English: {self.en}")
        print(f"Assamese: {self.as_marks}")
        print(f"Total Marks: {self.ctotal()}\n")

class ScienceStudent(Student):
    def __init__(self):
        super().__init__()
        self.sph = 0.0
        self.ch = 0.0
        self.ma = 0.0
        self.en = 0.0
    
    def takedata(self):
        super().getdata()
        self.sph = float(input("Enter Physics marks: "))
        self.ch = float(input("Enter Chemistry marks: "))
        self.ma = float(input("Enter Mathematics marks: "))
        self.en = float(input("Enter English marks: "))
    
    def ctotal(self):
        return self.sph + self.ch + self.ma + self.en
    
    def display(self):
        print(f"\n--- Science Student ---")
        print(f"Roll No: {self.rollno}")
        print(f"Name: {self.sname}")
        print(f"Physics: {self.sph}")
        print(f"Chemistry: {self.ch}")
        print(f"Mathematics: {self.ma}")
        print(f"English: {self.en}")
        print(f"Total Marks: {self.ctotal()}\n")

# Main program
choice = int(input("Enter 1 for Arts, 2 for Science: "))
if choice == 1:
    student = ArtsStudent()
    student.takedata()
    student.display()
else:
    student = ScienceStudent()
    student.takedata()
    student.display()
