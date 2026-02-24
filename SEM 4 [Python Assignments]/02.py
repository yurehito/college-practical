# Q2) WAP to take input of two numbers and print their sum, product, difference using operator choice
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *): ")

if op == '+':
    print("Sum:", a + b)
elif op == '-':
    print("Difference:", a - b)
elif op == '*':
    print("Product:", a * b)
else:
    print("Invalid operator")
