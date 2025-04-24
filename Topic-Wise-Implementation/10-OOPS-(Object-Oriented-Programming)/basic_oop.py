# some practice questions on Object-Oriented Programming (OOP) that you can use to test and improve your understanding

# Basic OOP Concepts:
# 1) Define a class called Car that has the following properties:

# brand
# model
# year
# color

# The class should have the following methods:
# A constructor (__init__) to initialize these properties.
# A method car_info() that prints the car's details (brand, model, year, and color).


class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def car_info(self):
        print(self.brand, self.model, self.year, self.color)


Car("BMW", "New", 2020, "Black").car_info()

# Create a class called BankAccount:
# Attributes: account_number, balance
# Methods:
# A constructor to initialize the account number and balance.
# A method deposit(amount) to deposit money.
# A method withdraw(amount) to withdraw money.
# A method check_balance() to display the current balance.


class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    # For Checking The Balance
    def check_balance(self):
        print(f"Balance {self.balance}")

    # For Debit
    def debit(self, amount):
        self.balance -= amount
        print(f"{amount} Debited Successfull New Balance {self.balance}")

    # For Credit
    def credit(self, amount):
        self.balance += amount
        print(f"{amount} Credit Successfull New Balance {self.balance}")


acc1 = Account(10000, 42201)
acc1.check_balance()
acc1.debit(5000)
acc1.credit(12000)

# Define a class called Student that represents a student:

# Attributes: name, age, grade
# Methods:
# A constructor to initialize the attributes.
# A method display_info() to print out the student's details.
# A method update_grade(new_grade) to change the student's grade.


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(
            f"The Student name is {self.name} age is {self.age} and the grade is {self.grade}"
        )

    def update_grade(self, new_grade):
        self.grade = new_grade
        self.display_info()


s1 = Student("Ammar", 19, "A+")
s1.display_info()
s1.update_grade("A")


# Create a class Rectangle:
# Attributes: length, width

# Methods:
# A constructor to initialize the rectangle's dimensions.
# A method area() to calculate and return the area of the rectangle.
# A method perimeter() to calculate and return the perimeter of the rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Area
    def calculate_area(self):
        return self.length * self.width

    # perimeter
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 10)
area = rect.calculate_area()
peri = rect.calculate_perimeter()
print(f"The Area Of A Rectangle is {area} and perimeter of a rectangle is {peri}")

# Create a class called Person:
# Attributes: name, age, gender
# Methods:
# A constructor to initialize the person’s details.
# A method greet() to print a greeting message that includes the person's name.


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f"Hello {self.name}")


p1 = Person("Umar Farooq", 17, "Male")
p1.greet()
