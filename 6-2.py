# Base class Publisher
class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name

    def display_info(self):
        return f"Publisher ID: {self.publisher_id}, Publisher Name: {self.publisher_name}"

# Derived class Book
class Book(Publisher):
    def __init__(self, publisher_id, publisher_name, title, author):
        # Invoke the base class constructor
        super().__init__(publisher_id, publisher_name)
        self.title = title
        self.author = author

    def display_info(self):
        # Override the display_info method to include Book-specific attributes
        publisher_info = super().display_info()  # Get publisher info from the base class
        return f"{publisher_info}, Title: {self.title}, Author: {self.author}"

# Derived class Python (subclass of Book)
class Python(Book):
    def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        # Invoke the base class constructor
        super().__init__(publisher_id, publisher_name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display_info(self):
        # Override the display_info method to include Python-specific attributes
        book_info = super().display_info()  # Get book info from the Book class
        return f"{book_info}, Price: ${self.price}, Number of Pages: {self.no_of_pages}"

# Taking input from the user
publisher_id = input("Enter Publisher ID: ")
publisher_name = input("Enter Publisher Name: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
price = float(input("Enter Book Price: $"))
no_of_pages = int(input("Enter Number of Pages: "))

# Create an object of Python class with the user input
python_book = Python(publisher_id, publisher_name, title, author, price, no_of_pages)

# Display the information about the Python book
print("\nInformation about the Python Book:")
print(python_book.display_info())

