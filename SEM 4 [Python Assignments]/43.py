# Question 43:
# Define an abstract base class figure and add to it pure virtual functions:
# display() : to display a figure
# get() : to input parameters of the figure
# area() : to compute the area of a figure
# perimeter() : to compute the perimeter of a figure.
# Derive three classes circle, rectangle and triangle from it. A circle is
# represented by its radius, rectangle by its length and breadth and
# triangle by the lengths of its sides. Write a main function and write necessary
# member functions to achieve run time polymorphism.

from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def display(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self):
        self.r = 0.0
    
    def get(self):
        self.r = float(input("Enter Radius: "))
    
    def display(self):
        print(f"Circle with radius {self.r}")
    
    def area(self):
        return math.pi * self.r * self.r
    
    def perimeter(self):
        return 2 * math.pi * self.r

class Rectangle(Figure):
    def __init__(self):
        self.length = 0.0
        self.breadth = 0.0
    
    def get(self):
        self.length = float(input("Enter Length: "))
        self.breadth = float(input("Enter Breadth: "))
    
    def display(self):
        print(f"Rectangle with length {self.length} and breadth {self.breadth}")
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Triangle(Figure):
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
    
    def get(self):
        self.a = float(input("Enter Side 1: "))
        self.b = float(input("Enter Side 2: "))
        self.c = float(input("Enter Side 3: "))
    
    def display(self):
        print(f"Triangle with sides {self.a}, {self.b}, {self.c}")
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

# Main program
figures = []
choice = int(input("Enter 1 for Circle, 2 for Rectangle, 3 for Triangle: "))

if choice == 1:
    fig = Circle()
elif choice == 2:
    fig = Rectangle()
else:
    fig = Triangle()

fig.get()
figures.append(fig)

for figure in figures:
    figure.display()
    print(f"Area: {figure.area():.2f}")
    print(f"Perimeter: {figure.perimeter():.2f}")
