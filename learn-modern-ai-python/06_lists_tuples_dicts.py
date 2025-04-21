# Working with Lists and Tuples
# Introduction: Python provides powerful sequence types: lists and tuples. These data structures help store and manage collections of data efficiently.

# 1. Lists in Python
# Lists are ordered, mutable, and indexed collections that can contain elements of different data types.

# Creating a List
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["hello", 42, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)

# Accessing List Elements
print(fruits[0])  # Output: apple
print(fruits[-3])  # Output: apple (Accessing element in reverse order)

# Modifying Lists
fruits[0] = "watermelon"  # Replacing "apple" with "watermelon"
print(fruits)  # Output: ['watermelon', 'banana', 'cherry']

# List Slicing
print(fruits[0:2])  # Output: ['watermelon', 'banana']

# 2. Common List Methods
# Appending and Extending Lists
fruits.append("mango")  # Adds a single element 'mango' to the end
print(fruits)  # Output: ['watermelon', 'banana', 'cherry', 'mango']

fruits.extend(["grape", "kiwi"])  # Adds multiple elements
print(fruits)  # Output: ['watermelon', 'banana', 'cherry', 'mango', 'grape', 'kiwi']

# Removing Elements
# remove() Method: Deletes the first occurrence of a specified value.
fruits.remove("banana")  # Removes 'banana'
print(fruits)  # Output: ['watermelon', 'cherry', 'mango', 'grape', 'kiwi']

# pop() Method: Removes an item at a specified index and returns the removed item.
deleted = fruits.pop(1)  # Removes and returns the element at index 1
print("deleted element = ", deleted)  # Output: 'cherry'
print(fruits)  # Output: ['watermelon', 'mango', 'grape', 'kiwi']

# Sorting a List
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()  # Sorts in ascending order
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

numbers.sort(reverse=True)  # Sorts in descending order
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]

# List Comprehension
squared = [x**2 for x in [1, 2, 3, 4, 5]]
print(squared)  # Output: [1, 4, 9, 16, 25]

# 3. Tuples in Python
# Tuples are ordered, immutable collections.

# Creating a Tuple
tuple1 = ("apple", "banana", "cherry")
tuple2 = (10, 20, 30)
mixed_tuple = ("hello", 42, 3.14, True)

print("tuple1 =", tuple1)
print("tuple2 =", tuple2)
print("mixed_tuple =", mixed_tuple)

# Accessing elements in a tuple
print("tuple1[0] =", tuple1[0])  # Output: apple

# Tuple Slicing
print("tuple2[1:] =", tuple2[1:])  # Output: (20, 30)

# Length of a Tuple
print("Length of tuple1:", len(tuple1))

# Iterating through a Tuple
for item in tuple2:
    print(item)  # Output: 10 20 30

# Checking if an item exists in a Tuple
print("Is 20 in tuple2?", 20 in tuple2)  # Output: True

# Concatenating Tuples
tuple3 = tuple1 + tuple2
print("tuple1 + tuple2 =", tuple3)

# Repeating Tuples
tuple4 = tuple2 * 2
print("tuple2 * 2 =", tuple4)

# 4. Dictionaries in Python
# A dictionary is a collection of key-value pairs.

# Creating a Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "visited_cities": ["New York", "Los Angeles", "Chicago"],
}
print(
    person
)  # Output: {'name': 'Alice', 'age': 25, 'visited_cities': ['New York', 'Los Angeles', 'Chicago']}

# Accessing Dictionary Values
print(person["name"])  # Output: Alice
print(person.get("age", "Not Found"))  # Output: 25

# Modifying a Dictionary
person["email"] = "alice@example.com"  # Adding a new key-value pair
person["age"] = 26  # Modifying an existing value
print(
    person
)  # Output: {'name': 'Alice', 'age': 26, 'visited_cities': ['New York', 'Los Angeles', 'Chicago'], 'email': 'alice@example.com'}

# Removing Items from a Dictionary
del person["email"]  # Removes the key "email"
print(
    person
)  # Output: {'name': 'Alice', 'age': 26, 'visited_cities': ['New York', 'Los Angeles', 'Chicago']}

# Using pop() to remove and return the value of a key
removed_value = person.pop("age")
print("Removed value:", removed_value)  # Output: 26
print(
    person
)  # Output: {'name': 'Alice', 'visited_cities': ['New York', 'Los Angeles', 'Chicago']}

# Dictionary Methods
print(person.keys())  # Output: dict_keys(['name', 'visited_cities'])
print(
    person.values()
)  # Output: dict_values(['Alice', ['New York', 'Los Angeles', 'Chicago']])
print(
    person.items()
)  # Output: dict_items([('name', 'Alice'), ('visited_cities', ['New York', 'Los Angeles', 'Chicago'])])

# Iterating Through a Dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary Comprehension
original_dict = {"a": 1, "b": 2, "c": 3}
doubled_dict = {k: v * 2 for k, v in original_dict.items()}
print(doubled_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}

# Practice Exercise: Celsius to Fahrenheit conversion using dictionary comprehension
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = {str(c) + "C": str((c * 9 / 5) + 32) + "F" for c in celsius_temps}
print(
    fahrenheit_temps
)  # Output: {'0C': '32.0F', '10C': '50.0F', '20C': '68.0F', '30C': '86.0F', '40C': '104.0F'}
