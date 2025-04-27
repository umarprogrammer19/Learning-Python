# Create a class Animal:

# Attributes: name, species

# Methods:
# A constructor to initialize these attributes.
# A method speak() that prints a generic sound for animals.

# Now, create two subclasses:
# Dog and Cat that inherit from Animal.
# Override the speak() method in both subclasses to print the respective sounds (e.g., "Woof" for dogs and "Meow" for cats).


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("Generic animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


Dog("Dog", "Dog").speak()
Cat("Cat", "Cat").speak()


# Define a class Shape with a method area():

# This method should be abstract (not implemented).
# Create subclasses for Circle, Square, and Triangle.
# Implement the area() method in each subclass.
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


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


print(Circle(5).area())
print(Square(5).area())
print(Triangle(5, 5).area())
