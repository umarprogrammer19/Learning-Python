# Python Data Types Example

# 1. Numeric Types

# Integer (int)
num_int: int = 42
print(type(num_int), " num_int = ", num_int)  # <class 'int'>  num_int =  42

# Floating-Point (float)
num_float: float = 3.14
print(type(num_float), " num_float = ", num_float)  # <class 'float'>  num_float =  3.14

# Complex (complex)
num_complex: complex = 2 + 3j
print(
    type(num_complex), " num_complex = ", num_complex
)  # <class 'complex'>  num_complex =  (2 + 3j)

# Accessing Real and Imaginary Parts of a Complex Number
z = 3 + 4j
print("Real Part:", z.real)  # Output: 3.0
print("Imaginary Part:", z.imag)  # Output: 4.0

# 2. Boolean (bool)
is_python_fun: bool = True  # False
print(
    type(is_python_fun), " is_python_fun = ", is_python_fun
)  # <class 'bool'>  is_python_fun =  True

# 3. Sequence Types (Ordered, Iterable)

# a. String (str)
text_double: str = "Hello, Python!"
text_single: str = "Hello, Python!"
text_multi: str = """Hello, Python!"""
text_multi_1: str = """Hello, Python!"""
print(
    type(text_double), " text_double = ", text_double
)  # <class 'str'>  text_double =  Hello, Python!
print(
    type(text_single), " text_single = ", text_single
)  # <class 'str'>  text_single =  Hello, Python!
print(
    type(text_multi), " text_multi = ", text_multi
)  # <class 'str'>  text_multi =  Hello, Python!
print(
    type(text_multi_1), " text_multi_1 = ", text_multi_1
)  # <class 'str'>  text_multi_1 =  Hello, Python!

# b. List (list)
my_list: list = [1, 2, 3, "Python", 3.14, 3 + 2j]
print(
    type(my_list), " my_list = ", my_list
)  # <class 'list'> my_list =  [1, 2, 3, 'Python', 3.14, (3+2j)]

# c. Tuple (tuple)
my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, 0.3, 3 + 2j)
print(
    type(my_tuple), " my_tuple = ", my_tuple
)  # <class 'tuple'>  my_tuple =  (1, 2, 3, 'AI', 2.71, False, 0.3, (3+2j))

# d. Range (range)
num_range: range = range(1, 10, 2)
print(
    type(num_range), " num_range = ", num_range.step
)  # <class 'range'> num_range =  2
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

# 4. Set Types

# a. Set (set)
my_set: set = {1, 2, 33, 4, 4, 5}
print(type(my_set), " my_set = ", my_set)  # <class 'set'> my_set =  {1, 2, 33, 4, 5}

# b. Frozen Set (frozenset)
frozen_set = frozenset([11, 2, 3, 4, 4, 5])
print(
    type(frozen_set), " frozen_set = ", frozen_set
)  # <class 'frozenset'>  frozen_set =  frozenset({1, 2, 33, 4, 5})

# 5. Mapping Type

# Dictionary (dict)
my_dict: dict = {"name": "Alice", "age": 25, "language": "Python"}
print(
    type(my_dict), " my_dict = ", my_dict
)  # <class 'dict'>  my_dict =  {'name': 'Alice', 'age': 25, 'language': 'Python'}

# 6. Binary Types

# a. Bytes (bytes)
byte_data: bytes = b"Hello"
print(
    type(byte_data), " byte_data = ", byte_data
)  # <class 'bytes'>  byte_data =  b'Hello'

# Open an image file in binary mode (example for binary files)
with open("Apollo11.jpg", "rb") as image_file:
    image_data = image_file.read()
    print(image_data)  # Prints raw binary data

# Write the binary data to a new image file
with open("copy.jpg", "wb") as target_file:
    target_file.write(image_data)
    print("Image copied successfully!")  # Output: Image copied successfully!

# b. Bytearray (bytearray)
byte_array: bytearray = bytearray([65, 66, 67, 69])  # 65=A, 66=B .... in decimal system
print(
    type(byte_array), " byte_array = ", byte_array
)  # <class 'bytearray'>  byte_array =  bytearray(b'ABCE')
print(byte_array[0])  # Output: 65
print(chr(byte_array[0]))  # Output: 'A'

# c. Memoryview (memoryview)
mem_view: memoryview = memoryview(b"Operation Badar")
print(
    type(mem_view), " mem_view = ", mem_view
)  # <class 'memoryview'> mem_view =  <memory at 0x7d294da28b80>
print(bytes(mem_view[0:5]))  # Output: b'Opera'
print(mem_view[6:11])  # Output: <memory at 0x7d294da28f40>

# 7. None Data Type in Python
# None represents the absence of a value or null object reference.

x: str = None
y: str = None
z: str = x
print(type(x))  # <class 'NoneType'>
print("value of x = " + str(x))  # value of x = None
print("x == y = ", x == y)  # True
print("x is y = ", x is y)  # True
print("id(x) == id(z) = ", id(x) == id(z))  # True

# Checking None in conditional statements
if None:
    print("This line will not execute because None is False")
else:
    print("Else block: As None is considered False, this line of code will execute")

# 8. Integer Literals in Python (Memory Space Sharing)

x: int = 1
y: int = 1
z: int = x
print(
    "Value of x = " + str(x) + ", and id(x) = " + str(id(x))
)  # same object memory for small integers
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(z) = " + str(id(z)))

# Integer Interning Example (for integers between -5 and 256)
a = -6
b = -6
c = a
print("Value of a = " + str(a) + ", and id(a) = " + str(id(a)))
print("Value of b = " + str(b) + ", and id(b) = " + str(id(b)))
print("Value of c = " + str(c) + ", and id(c) = " + str(id(c)))

# 9. Type Casting

i: int = 10
j: float = 20.6
f: float = i + j  # Implicit type casting
print(
    "Value of f = " + str(f) + ", Type of f = " + str(type(f))
)  # Implicit casting int to float

f1: float = 66.89
i1: int = int(f1)  # Explicit type casting: float to int
print(
    "Value of i1 = " + str(i1) + ", Type of i = " + str(type(i1))
)  # Truncates decimal part

s: str = "25.8"
f2: float = float(s)  # Explicit type casting: string to float
print("Value of f2 = " + str(f2) + ", Type of i = " + str(type(f2)))

# Error handling for incorrect type casting
try:
    i2 = int(s)  # This would fail as 's' is a string representing a float
except ValueError as e:
    print("Error:", e)

# 10. Truthy and Falsy Values

k: int = -9  # Any non-zero integer is truthy
b: bool = bool(k)
print("Value of b = " + str(b) + ", Type of b = " + str(type(b)))  # True

if k:
    print("if block: This line of code will execute if k is non-zero")
else:
    print("else block: This line of code will not execute")

# 11. Using isinstance() Function

age: int = 20
weight: float = 66.89
print("check: isinstance(age, int) = ", isinstance(age, int))  # True
print("check: isinstance(weight, int) = ", isinstance(weight, int))  # False
print("check: isinstance(weight, float) = ", isinstance(weight, float))  # True
