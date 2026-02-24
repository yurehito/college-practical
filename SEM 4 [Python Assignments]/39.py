# Question 39:
# Define an abstract base class printer. Derive three classes laser-printer,
# line-printer and inkjet-printer. The derived classes will have data members
# to store the features of particular printer. Write pure virtual function
# display() in the base class and redefine it in the derived classes.

class Printer:
    def __init__(self):
        pass
    
    def display(self):
        raise NotImplementedError("Subclasses must implement display()")

class LaserPrinter(Printer):
    def __init__(self):
        super().__init__()
        self.model = ""
        self.ppm = 0
    
    def getdata(self):
        self.model = input("Enter Model: ")
        self.ppm = int(input("Enter Pages Per Minute: "))
    
    def display(self):
        print(f"Laser Printer: {self.model} - {self.ppm} ppm\n")

class LinePrinter(Printer):
    def __init__(self):
        super().__init__()
        self.name = ""
    
    def getdata(self):
        self.name = input("Enter LinePrinter Name: ")
    
    def display(self):
        print(f"LinePrinter: {self.name}\n
