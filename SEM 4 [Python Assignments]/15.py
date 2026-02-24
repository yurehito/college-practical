# Q15) WAP to print all prime numbers between two given numbers
start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Prime numbers between", start, "and", end, ":")
num = start
while num <= end:
    if num > 1:
        i = 2
        is_prime = True
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i = i + 1
        if is_prime:
            print(num, end=" ")
    num = num + 1
print()
