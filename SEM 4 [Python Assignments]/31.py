# Question 31:
# Define a class named "triangle" to represent a triangle using the lengths
# of the three sides. Write a constructor to initialize objects of this class,
# and write member functions to check
# (a) if a triangle is isosceles
# (b) if a triangle is equilateral
# Write a main function to test your functions.

class Triangle:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
    
    def is_isosceles(self):
        return (self.a == self.b) or (self.b == self.c) or (self.a == self.c)
    
    def is_equilateral(self):
        return (self.a == self.b) and (self.b == self.c)

# Main function to test
x, y, z = map(float, input("Enter three sides: ").split())

t = Triangle(x, y, z)

if t.is_equilateral():
    print("Equilateral\n")
elif t.is_isosceles():
    print("Isosceles\n")
else:
    print("Scalene\n")
