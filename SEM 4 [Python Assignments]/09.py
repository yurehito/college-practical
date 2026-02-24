# Q9) WAP to find factorial of a given number using loop
n = int(input("Enter a non-negative integer: "))
fact = 1

if n < 0:
    print("Factorial not defined")
else:
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print("Factorial:", fact)