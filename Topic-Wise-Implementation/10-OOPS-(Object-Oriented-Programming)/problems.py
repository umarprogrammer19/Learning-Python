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
