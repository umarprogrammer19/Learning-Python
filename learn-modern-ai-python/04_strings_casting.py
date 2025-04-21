# Strings in Python

# Creating Strings
my_string_single: str = "Hello, World!"  # Single Quotes
my_string_double: str = "Hello, World!"  # Double Quotes
my_string_triple: str = """Hello, World!"""  # Triple Quotes (multi-line)
my_string_raw: str = r"Hello\tWorld"  # Raw String (backslashes are treated literally)

# Printing different types of strings
print(my_string_single)  # Output: Hello, World!
print(my_string_triple)  # Output: Hello, World! (multi-line)
print(my_string_raw)  # Output: Hello\tWorld

# Escape Sequence Characters
print("Hello,\b World!")  # \b backspace
print("Hello,\tWorld!")  # \t tab
print('Hello, "World!"')  # \" for double quotes inside string
print("Hello,\\ World!")  # \\ for backslash inside string

# Unicode Characters
print(r"\u0041 = ", "\u0041")  # Unicode for 'A'
print(r"\u0042 = ", "\u0042")  # Unicode for 'B'
print(r"\u0043 = ", "\u0043")  # Unicode for 'C'

# Operations on Strings

# Concatenation
my_string = "Hello, " + "World!"
print(my_string)  # Output: Hello, World!

# Indexing (strings are zero-indexed)
print(my_string[1])  # Output: e (second character)

# Slicing
print(my_string[7:])  # Output: World! (from index 7 to end)
print(my_string[0:5])  # Output: Hello (from index 0 to 4)

# Length of the string
print(len(my_string))  # Output: 13 (counts characters including spaces)

# Upper and Lower Case
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.lower())  # Output: hello, world!

# String Methods: Split, Join, Replace, Find, Count

# Split string into list of substrings
words = my_string.split()  # Split by space
print(words)  # Output: ['Hello,', 'World!']

# Join list of strings into a single string
joined_string = ", ".join(["Pakistan", "USA", "Canada", "France", "Japan"])
print(joined_string)  # Output: Pakistan, USA, Canada, France, Japan

# Replace substring in a string
my_string = "Hello, World! Hello, Pakistan"
my_string = my_string.replace("Hello", "Salam Walikum")
print(my_string)  # Output: Salam Walikum, World! Salam Walikum, Pakistan

# Find index of substring
starting_index = my_string.find("Salam")  # Finds first occurrence
print("Starting index of Salam: ", starting_index)  # Output: 0

# Count occurrences of a substring
count = my_string.count("Salam")  # Count how many times 'Salam' appears
print("Count of 'Salam': ", count)  # Output: 2

# String Formatting

# Using the % operator (older method)
name = "John"
age = 20
my_string = "My name is %s, and I am %d years old" % (name, age)
print(my_string)  # Output: My name is John, and I am 20 years old

# Using str.format() (newer method)
my_string = "My name is {} and I am {} years old".format(name, age)
print(my_string)  # Output: My name is John and I am 20 years old

# Using f-strings (Best for readability and efficiency)
my_string = f"My name is {name} and I am {age} years old"
print(my_string)  # Output: My name is John and I am 20 years old

# String Repetition
base_string = "Hello"
repeated_string = base_string * 3
print(f"Repeated string: {repeated_string}")  # Output: HelloHelloHello

# Using string repetition for visual separators
separator = "-" * 30
print(separator)  # Output: ------------------------------

# Comparison Operators for Strings
str1 = "apple"
str2 = "banana"

print("str1 == str2: ", str1 == str2)  # Output: False
print("str1 != str2: ", str1 != str2)  # Output: True
print("str1 > str2: ", str1 > str2)  # Output: False
print("str1 < str2: ", str1 < str2)  # Output: True

# Using Comparison Operators in if statements
word = "mango"
if word > "apple":
    print(f"{word} comes after apple in alphabetical order")
else:
    print(f"{word} comes before apple in alphabetical order")

# Type Casting in Python

# Implicit Type Casting (Automatic)
num_int = 10
num_float = num_int + 5.5  # int + float automatically converts to float
print(num_float, type(num_float))  # Output: 15.5 <class 'float'>

# Explicit Type Casting (Manual)
num_str = "100"
num_int = int(num_str)  # Convert string to integer
print(num_int, type(num_int))  # Output: 100 <class 'int'>

# Converting int to float
num_float = float(num_int)  # Convert integer to float
print(num_float, type(num_float))  # Output: 100.0 <class 'float'>

# Converting int to complex
num_complex = complex(num_int)  # Convert integer to complex
print(num_complex, type(num_complex))  # Output: (100+0j) <class 'complex'>

# Converting float to int (will truncate the decimal part)
num_float = 9.8
num_int = int(num_float)  # Removes decimal part
print(num_int, type(num_int))  # Output: 9 <class 'int'>

# Converting bool to int
bool_val = True
print(int(bool_val))  # Output: 1 (True is 1)

# Converting bool to string
print(str(bool_val))  # Output: "True"

# Converting list to set (removes duplicates)
lst = [1, 2, 2, 3, 4, 4, 5]
s = set(lst)
print(s, type(s))  # Output: {1, 2, 3, 4, 5} <class 'set'>

# Converting list of tuples to dictionary
lst = [("name", "Alice"), ("age", 25)]
d = dict(lst)
print(d, type(d))  # Output: {'name': 'Alice', 'age': 25} <class 'dict'>
