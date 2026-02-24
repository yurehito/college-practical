# Q16) WAP to find sum of first n natural numbers
n = int(input("Enter a positive integer: "))
if n < 1:
    print("Enter positive integer")
else:
    total = n * (n + 1) // 2
    print("Sum =", total)
