# Modules in Python

# A module in Python is a file containing Python definitions and statements. The file can define functions, classes, and variables.
# Modules are used to organize and reuse code efficiently.

# Example of using Built-in Module
import math

print(math.sqrt(25))  # Output: 5.0

# Example of using External Module
# Install a third-party module using pip:
# !pip install requests
import requests

response = requests.get("https://fakestoreapi.com/products/")
print(response.status_code)  # Output: 200

# How to Import Modules
import math  # Basic import

print(math.pi)  # Output: 3.141592653589793

import numpy as np  # Import with alias

print(np.array([1, 2, 3]))  # Output: [1 2 3]

from math import sqrt, pi  # Import specific functions

print(sqrt(16))  # Output: 4.0
print(pi)  # Output: 3.141592653589793

from math import *  # Import everything (not recommended for large modules)

print(sin(0))  # Output: 0.0

# Function Definition in Python

# A function is a block of code that performs a specific task. Functions are reusable and help organize code.


def my_function():
    print("Hello, World!")


my_function()  # Output: Hello, World!

# Types of Functions
# Built-in Functions
print("Hello, World!")  # Example of a built-in function

# Functions defined in built-in modules
import random

print(random.random())  # Output: Random float between 0 and 1


# User-Defined Functions
def my_function():
    print("Hello, Operation Badar")


my_function()  # Output: Hello, Operation Badar


# Function Syntax
def greetings():
    "This is docstring of greetings function"
    greet = "Hello World!"
    return greet


message = greetings()
print(message)  # Output: Hello World!

# Pass by Reference vs Value in Functions
# Immutable objects (e.g., integers) remain unchanged, while mutable objects (e.g., lists) can be modified.


def modify_value(x):
    x = 10
    print("Within function:", x)


x = 5
print("Original:", x)
modify_value(x)
print("After function:", x)

# Immutable object (integer)
# Output:
# Original: 5
# Within function: 10
# After function: 5


def modify_list(lst):
    lst.append(4)
    print("Within function:", lst)


lst = [1, 2, 3]
print("Original:", lst)
modify_list(lst)
print("After function:", lst)

# Mutable object (list)
# Output:
# Original: [1, 2, 3]
# Within function: [1, 2, 3, 4]
# After function: [1, 2, 3, 4]


# Function Arguments
def greetings(name):
    print("Hello {}".format(name))


greetings("Ali")  # Output: Hello Ali
greetings("Umar")  # Output: Hello Umar


# Keyword Arguments
def printinfo(name, age):
    print("Name:", name)
    print("Age:", age)


printinfo(age=50, name="Arif")
# Output:
# Name: Arif
# Age: 50


# Default Arguments
def printinfo(name, age=35):
    print("Name:", name)
    print("Age:", age)


printinfo(name="Arif", age=50)  # Output: Name: Arif, Age: 50
printinfo(name="Arif")  # Output: Name: Arif, Age: 35


# Arbitrary Arguments using *args
def printinfo(arg1, *vartuple):
    print("Output is:")
    print(arg1)
    for var in vartuple:
        print("*", var)


printinfo(10)
printinfo(70, 60, 50, 70, 90)


# Arbitrary Keyword Arguments using **kwargs
def my_function(**student):
    print("His last name is " + student["lname"])
    for key, value in student.items():
        print(key, value)
    print(student)


my_function(
    fname="Ali", lname="Osman"
)  # Output: His last name is Osman, fname: Ali, lname: Osman


# Multi-type Return in Functions
def example_function(a: int, b: int = 0, *args: float, **kwargs: str):
    sum_ab = a + b
    args_list = list(args)
    return sum_ab, args_list, kwargs


result = example_function(1, 2, 3.14, 2.71, name="Alice", city="New York")
print(result)

# Output: (3, [3.14, 2.71], {'name': 'Alice', 'city': 'New York'})

# Lambda Functions
# Anonymous functions in Python using lambda

add_two = lambda x, y: x + y
print(add_two(1, 2))  # Output: 3

# Sort a dictionary using lambda function
my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)  # Output: {'date': 1, 'banana': 2, 'apple': 5, 'cherry': 8}


# Recursion in Python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120

# Generator Functions
# A generator function is a function that yields values instead of returning them, allowing iteration over them.


def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()
for value in gen:
    print(value)  # Output: 1, 2, 3


# Infinite Sequence using Generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
for _ in range(5):
    print(next(gen))  # Output: 0, 1, 2, 3, 4

# Generator Expressions
gen_expr = (x * x for x in range(5))
for value in gen_expr:
    print(value)  # Output: 0, 1, 4, 9, 16