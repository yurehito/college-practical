# Q30) WAP to check whether a number is Armstrong number or not
num = int(input("Enter a number: "))
temp = num
s = 0

digits = 0
t = temp
if t == 0:
    digits = 1
else:
    while t != 0:
        digits = digits + 1
        t = t // 10

while temp != 0:
    d = temp % 10
    s = s + (d ** digits)
    temp = temp // 10

if s == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
