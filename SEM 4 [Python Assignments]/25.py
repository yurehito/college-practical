# Q25) WAP to count number of vowels, consonants, digits and spaces in a string
s = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for ch in s:
    if ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u':
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch.isspace():
        spaces = spaces + 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)