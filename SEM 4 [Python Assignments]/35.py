# Question 35:
# Create a class "Book" with the following specifications:
# isbn : ISBN number (string)
# title : Book title (string)
# author : Author name (string)
# price : Price (float)
# getdata() : to read the data
# dispdata() : to display the data
# search(author_name) : to search books by author name
# Write a main program.

class Book:
    def __init__(self):
        self.isbn = ""
        self.title = ""
        self.author = ""
        self.price = 0.0
    
    def getdata(self):
        self.isbn = input("Enter ISBN: ")
        self.title = input("Enter Title: ")
        self.author = input("Enter Author: ")
        self.price = float(input("Enter Price: "))
    
    def dispdata(self):
        print(f"ISBN: {self.isbn}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
    
    def search(self, author_name):
        if self.author.lower() == author_name.lower():
            return True
        return False

# Main program
book = Book()
book.getdata()
book.dispdata()
author_search = input("Enter author name to search: ")
if book.search(author_search):
    print("Book found by this author")
else:
    print("Book not found by this author")
