# Q29) WAP to search an element in a list (linear search)
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid size")
else:
    arr = []
    i = 0
    while i < n:
        val = int(input("Enter element " + str(i + 1) + ": "))
        arr.append(val)
        i = i + 1

    key = int(input("Enter element to search: "))

    pos = -1
    i = 0
    while i < n:
        if arr[i] == key:
            pos = i + 1
            break
        i = i + 1

    if pos == -1:
        print("Element not found")
    else:
        print("Element found at position", pos)
