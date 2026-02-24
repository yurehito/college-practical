# Q12) WAP to reverse a given integer
num = int(input("Enter an integer: "))
n = abs(num)
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10

if num < 0:
    rev = -rev

print("Reversed number:", rev)