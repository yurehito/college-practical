# Q28) WAP to sort a list (array) of numbers in ascending order
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

    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j = j + 1
        i = i + 1

    print("Sorted list:", arr)
