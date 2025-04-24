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
e1.increase_salary(10) # 55000 + 10%

m1 = Manager("Umar Farooq", 50000, "Development")
m1.increase_salary(10) # 60000 + 20%
