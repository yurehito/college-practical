# Q10) WAP to generate multiplication table of a given number
n = int(input("Enter number: "))
limit = int(input("Enter limit (e.g. 10): "))

i = 1
while i <= limit:
    print(n, "x", i, "=", n * i)
    i = i + 1