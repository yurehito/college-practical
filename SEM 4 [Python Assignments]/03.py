# Q3) WAP to find the smallest and largest of three numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

smallest = n1
if n2 < smallest:
    smallest = n2
if n3 < smallest:
    smallest = n3

largest = n1
if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3

print("Smallest:", smallest)
print("Largest:", largest)
