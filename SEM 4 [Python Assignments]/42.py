# Question 42:
# Define an abstract base class printer. Derive three classes laser-printer,
# line-printer and inkjet-printer. The derived classes will have data members
# to store the features of that particular printer. Write pure virtual function
# display() in the base class and redefine it in the derived classes.

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def display(self):
        pass

class LaserPrinter(Printer):
    def __init__(self):
        self.model = ""
        self.ppm = 0
    
    def getdata(self):
        self.model = input("Enter Model: ")
        self.ppm = int(input("Enter Pages Per Minute: "))
    
    def display(self):
        print(f"Laser Printer - Model: {self.model}, PPM: {self.ppm}\n")

class LinePrinter(Printer):
    def __init__(self):
        self.name = ""
    
    def getdata(self):
        self.name = input("Enter LinePrinter Name: ")
    
    def display(self):
        print(f"LinePrinter - Name: {self.name}\n")

class InkjetPrinter(Printer):
    def __init__(self):
        self.type = ""
    
    def getdata(self):
        self.type = input("Enter Inkjet Printer Type: ")
    
    def display(self):
        print(f"Inkjet Printer - Type: {self.type}\n")

# Main program
printers = []
choice = int(input("Enter 1 for Laser, 2 for Line, 3 for Inkjet: "))

if choice == 1:
    laser = LaserPrinter()
    laser.getdata()
    printers.append(laser)
elif choice == 2:
    line = LinePrinter()
    line.getdata()
    printers.append(line)
elif choice == 3:
    inkjet = InkjetPrinter()
    inkjet.getdata()
    printers.append(inkjet)

for printer in printers:
    printer.display()
