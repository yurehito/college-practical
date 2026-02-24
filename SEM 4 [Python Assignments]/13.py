# Q13) WAP to check whether a given number is palindrome or not
num = int(input("Enter an integer: "))
if num < 0:
    print("Negative numbers not considered")
else:
    temp = num
    rev = 0
    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10
    if rev == num:
        print("Palindrome number")
    else:
        print("Not a palindrome")