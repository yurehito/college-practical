# Q11) WAP to print Fibonacci series up to n terms
n = int(input("Enter number of terms: "))
a = 0
b = 1
count = 0

if n <= 0:
    print("Enter positive integer")
else:
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count = count + 1
    print()