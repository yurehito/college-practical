# Q27) WAP to find smallest element in a list (array)
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid size")
else:
    arr = []
    i = 0
    while i < n:
        val = float(input("Enter element " + str(i + 1) + ": "))
        arr.append(val)
        i = i + 1

    smallest = arr[0]
    i = 1
    while i < n:
        if arr[i] < smallest:
            smallest = arr[i]
        i = i + 1

    print("Smallest element:", smallest)
