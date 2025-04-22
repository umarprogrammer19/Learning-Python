# class is a blueprint for creating an object


# creating class
class Student:
    name = "Umar Farooq"


# creating object (instance)
s1 = Student()
print(s1.name)

# Constructor it is basically the __init__ function it is invoked at a time of object creation
# All classes have a function called __init__(), which is always executed when the object is being initiated.


class Car:
    def __init__(self):
        print("Adding New Car In A Garage")


car1 = (
    Car()
)  # We cant print anything but the print("Adding New Car In A Garage") runs because constructor is always executed when the object is being initiated.


# self: The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


class Animal:

    # Default Constructor python makes it self we do not need to make it
    # def __init__(self):
    #     pass

    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Animal("Cow", 2)
print(f"The name of a animal is {a.name} and age is {a.age}")


# Methods
# Methods are functions that belong to objects.


class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


s1 = User("Umar")
s1.greet()
# print(s1.name)


# Static Methods
# Methods that don’t use the self parameter (work at class level)
class Stu:
    @staticmethod # this is a decorator
    # Decorators allow us to wrap another function in order to
    # extend the behaviour of the wrapped function, without
    # permanently modifying it
    def college():
        print("ABC College")


Stu.college()
