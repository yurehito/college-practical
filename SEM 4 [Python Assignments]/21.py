# Q21) WAP to swap two numbers without using a temporary variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swap: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swap: a =", a, "b =", b)