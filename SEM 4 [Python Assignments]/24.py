# Q24) WAP to check whether a character is vowel or consonant
ch = input("Enter a single character: ")
if len(ch) != 1 or not ch.isalpha():
    print("Enter one alphabet character")
else:
    if ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u':
        print("Vowel")
    else:
        print("Consonant")