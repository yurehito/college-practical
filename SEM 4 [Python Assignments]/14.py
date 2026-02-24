# Q14) WAP to check whether a number is prime or not
n = int(input("Enter a positive integer: "))

if n <= 1:
    print("Not a prime number")
else:
    i = 2
    is_prime = True
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i = i + 1

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
