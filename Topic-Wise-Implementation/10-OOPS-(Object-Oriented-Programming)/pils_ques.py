# Qs: Define a Circle class to create a circle with radius r using the constructor. Define and Area() method of the class which calculates the area of the circle. Define a Parameter() method of the class which allows you to calculate the parimeter of the circle

import math


class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius**2)

    def perimeter(self):
        return 2 * self.pi * self.radius


c = Circle(5)
print(c.area())
print(c.perimeter())

# Qs: Define a Employee class with attribute role ,department & salary. This class also has a showDetails() method.
# Create An Engineer class that inherits properties from Employee & has additional attributes: name and age


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(
            f"The role of an employee is {self.role}, department of an employee is {self.department} and the salary of an employee is {self.salary}"
        )


class Engineer(Employee):
    def __init__(self, role, department, salary, name, age):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age


e1 = Engineer("Employee", "Development", 50000, "Ammar", 20)
e1.show_details()
