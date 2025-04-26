# Intermediate OOP Concepts:

# 1) Create a class Shape:
# This should be a base class for different shapes.
# Include an abstract method area() which must be overridden in any subclass.
# Now, create two subclasses:
# Circle and Rectangle that inherit from Shape.
# In the Circle class, override area() to return the area of the circle.
# In the Rectangle class, override area() to return the area of the rectangle.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 2) Implement a class Employee:

# Attributes: name, salary
# Methods:
# A constructor to initialize the name and salary.
# A method increase_salary(percentage) to increase the salary by a given percentage.
# A method display_salary() to print the salary.
# Now, create a subclass Manager that inherits from Employee:
# Add an additional attribute department.
# Override the method increase_salary() to increase the salary by 10% more than the given percentage (for managers).


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary = self.salary * (1 + (percentage / 100))
        self.display_salary()

    def display_salary(self):
        print(f"Salary: {int(self.salary)}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def increase_salary(self, percentage):
        total_percentage = percentage + 10
        self.salary = self.salary * (1 + (total_percentage / 100))
        self.display_salary()


e1 = Employee("Ammar", 50000)
e1.increase_salary(10)  # 55000 + 10%

m1 = Manager("Umar Farooq", 50000, "Development")
m1.increase_salary(10)  # 60000 + 20%

# Create a class Book:
# Attributes: title, author, pages

# Methods:
# A constructor to initialize these attributes.
# A method book_summary() that displays a summary of the book with title, author, and number of pages.
# Now, create a subclass Ebook that adds an additional attribute file_size (in MB).
# Override the book_summary() method to include the file_size.


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"


class Ebook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def book_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, File Size: {self.file_size}MB"


b = Book("Harry Porter", "Ammar", 200)
print(b.book_summary())
b2 = Ebook("Harry Porter", "Ammar", 200, 100)
print(b2.book_summary())

# Define a class Shape3D:
# Attributes: length, width, height
# Methods:
# A constructor to initialize these attributes.
# A method volume() to calculate the volume of the 3D shape (rectangular prism).
# Now, create a subclass Cube that inherits from Shape3D:
# Override the volume() method to calculate the volume of a cube using the length.


class Shape3D:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


class Cube(Shape3D):
    def __init__(self, length):
        super().__init__(length, length, length)

    def volume(self):
        return self.length**3


s = Cube(10)
print(s.volume())

# Create a class Library:
# Attributes: books (a list of book titles)

# Methods:
# A constructor to initialize the list of books.
# A method add_book(book_name) to add a book to the library.
# A method remove_book(book_name) to remove a book from the library.
# A method show_books() to display the list of all available books.


class Library:
    def __init__(self, books):
        if isinstance(books, list):
            self.books = books
        else:
            return

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book {book_name} Added Successfully In The Library")
        self.show_books()

    def remove_book(self, book_name):
        self.books.remove(book_name)
        print(f"Book {book_name} Removed Successfully From The Library")
        self.show_books()

    def show_books(self):
        print(self.books)


book = Library(["Book 1", "Book 2", "Book 3"])
book.show_books()
book.remove_book("Book 1")
book.remove_book("Book 2")
book.add_book("Book 4")
book.add_book("Book 5")
