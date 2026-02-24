# Q17) WAP to find sum of digits of a number
num = int(input("Enter an integer: "))
n = abs(num)
s = 0

while n > 0:
    s = s + (n % 10)
    n = n // 10

print("Sum of digits:", s)
