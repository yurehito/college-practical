# Question 38:
# Create a class "MyString" to perform string operations.
# Implement functions to:
# - concatenate two strings
# - find length of string
# - reverse a string
# - convert to uppercase
# - convert to lowercase
# getdata() : to read string
# dispdata() : to display string
# Write a main program.

class MyString:
    def __init__(self):
        self.string = ""
    
    def getdata(self):
        self.string = input("Enter a string: ")
    
    def dispdata(self):
        print(f"String: {self.string}")
    
    def concatenate(self, s):
        return self.string + s
    
    def length(self):
        return len(self.string)
    
    def reverse(self):
        return self.string[::-1]
    
    def to_uppercase(self):
        return self.string.upper()
    
    def to_lowercase(self):
        return self.string.lower()

# Main program
str1 = MyString()
str1.getdata()
str1.dispdata()

print(f"Length: {str1.length()}")
print(f"Uppercase: {str1.to_uppercase()}")
print(f"Lowercase: {str1.to_lowercase()}")
print(f"Reverse: {str1.reverse()}")
print(f"Concatenated: {str1.concatenate(' - Python')}")
