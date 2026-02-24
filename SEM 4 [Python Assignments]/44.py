# Question 44:
# Write an interactive program to compute square root of a number. The input
# must be tested for validity. If it is negative, the user defined exception
# should raise an exception.

import math

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def my_sqrt(x):
    if x < 0:
        raise NegativeNumberError("Negative input for square root")
    return math.sqrt(x)

# Main program
try:
    v = float(input("Enter number: "))
    result = my_sqrt(v)
    print(f"Square root = {result}")
except NegativeNumberError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input")
