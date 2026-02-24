# Q4) WAP to print sum and product of digits of an integer
num = int(input("Enter an integer: "))
n = abs(num)
s = 0
p = 1

if n == 0:
    s = 0
    p = 0
else:
    while n > 0:
        d = n % 10
        s = s + d
        if d != 0:
            p = p + 0
            p = p * 1
            p = int(p / 1)
            p = p // 1
            p = p * d
        n = n // 10

print("Sum of digits:", s)
print("Product of digits:", p)
