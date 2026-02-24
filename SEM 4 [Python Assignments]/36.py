# Question 36:
# Define a class "Complex" to represent complex numbers with operations
# real : real part (float)
# imag : imaginary part (float)
# add(c1, c2) : to add two complex numbers
# subtract(c1, c2) : to subtract two complex numbers
# multiply(c1, c2) : to multiply two complex numbers
# getdata() : to read the data
# dispdata() : to display the data
# Write a main program.

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    
    def add(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)
    
    def subtract(self, c):
        return Complex(self.real - c.real, self.imag - c.imag)
    
    def multiply(self, c):
        real_part = (self.real * c.real) - (self.imag * c.imag)
        imag_part = (self.real * c.imag) + (self.imag * c.real)
        return Complex(real_part, imag_part)
    
    def getdata(self):
        self.real = float(input("Enter real part: "))
        self.imag = float(input("Enter imaginary part: "))
    
    def dispdata(self):
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} {self.imag}i")

# Main program
c1 = Complex()
c2 = Complex()
print("Enter first complex number:")
c1.getdata()
print("Enter second complex number:")
c2.getdata()

result_add = c1.add(c2)
result_sub = c1.subtract(c2)
result_mul = c1.multiply(c2)

print("Addition: ", end="")
result_add.dispdata()
print("Subtraction: ", end="")
result_sub.dispdata()
print("Multiplication: ", end="")
result_mul.dispdata()
