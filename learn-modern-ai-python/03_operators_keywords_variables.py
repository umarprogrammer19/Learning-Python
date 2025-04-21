# 1. Operators and Operands

# Unary Operators
# Negative (-): Changes the sign of the operand
x = 5
y = -x  # y is now -5
print("y = ", y)  # Output: -5

# Logical NOT (not): Reverses a boolean value
a = True
b = not a  # b is now False
print("b = ", b)  # Output: False

# Bitwise NOT (~): Inverts the bits of a number
x = 5  # Binary: 0101
y = ~x  # y is now -6 (binary: 1010, in two's complement)
print("y = ", y)  # Output: -6

# Convert integer to binary
print("bin(x) = ", bin(x), type(bin(x)))  # Output: bin(x) =  0b101 <class 'str'>
print(format(x, "b"))  # Output: 101
print(f"{x:b}")  # Output: 101

# Binary Operators
# Arithmetic Operations
a, b = 10, 3
print("a + b = ", a + b)  # Output: 13
print("a - b = ", a - b)  # Output: 7
print("a * b = ", a * b)  # Output: 30
print("a / b = ", a / b)  # Output: 3.3333333333333335
print("a // b = ", a // b)  # Output: 3
print("a % b = ", a % b)  # Output: 1
print("a ** b = ", a**b)  # Output: 1000

# Comparison Operators
x, y = 10, 5
print("x == y = ", x == y)  # Output: False
print("x != y = ", x != y)  # Output: True
print("x > y = ", x > y)  # Output: True
print("x < y = ", x < y)  # Output: False
print("x >= y = ", x >= y)  # Output: True
print("x <= y = ", x <= y)  # Output: False

# Logical Operators
x, y = True, False
print("x and y = ", x and y)  # Output: False
print("x or y = ", x or y)  # Output: True
print("not x = ", not x)  # Output: False

# Assignment Operators
x = 5
print("x = 5: ", x)  # Output: 5
x += 3
print("x += 3: ", x)  # Output: 8
x -= 3
print("x -= 3: ", x)  # Output: 5
x *= 3
print("x *= 3: ", x)  # Output: 15
x /= 3
print("x /= 3: ", x)  # Output: 5.0
x //= 3
print("x //= 3: ", x)  # Output: 1.0

# Identity Operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a is c = ", a is c)  # Output: True (same object)
print("a is b = ", a is b)  # Output: False (different objects)
print("a == b = ", a == b)  # Output: True (same values)
print("a is not b = ", a is not b)  # Output: True

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("3 in my_list = ", 3 in my_list)  # Output: True
print("10 not in my_list = ", 10 not in my_list)  # Output: True

my_string = "Operation Badar"
print("'O' in my_string = ", "O" in my_string)  # Output: True
print("'Hello' not in my_string = ", "Hello" not in my_string)  # Output: True

# 2. Python Keywords
import keyword

print("Python Keywords: ", keyword.kwlist) # Python Keywords:  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 3. Variable Management
# Valid variable names
name = "Alice"
_age = 25
salary2024 = 50000
my_variable = "Python"

# Invalid variable names (uncomment to see error)
# 2name = "Bob"  # Starts with a digit
# my-variable = "Error"  # Contains a hyphen
# class = "CS101"  # Reserved keyword

# Assigning multiple values simultaneously
x, y, z = 1, 2.5, "Python"
print(x, y, z)  # Output: 1 2.5 Python

# Delete a variable using del
x = 10
print(x)  # Output: 10
del x
# print(x)  # Uncommenting this will raise NameError: name 'x' is not defined

# 4. Truthy and Falsy Values
k = -9
b = bool(k)
print("Value of b = ", b, ", Type of b = ", type(b))  # Output: True

if k:
    print("if block: This line of code will execute if k is non-zero")
else:
    print("else block: This line of code will not execute")

print("\n =================== \n")
print("check: bool('55') = ", bool("55"))  # Output: True
print("check: bool('') = ", bool(""))  # Output: False
print("check: bool([1, 2, 3]) = ", bool([1, 2, 3]))  # Output: True
print("check: bool({}) = ", bool({}))  # Output: False

# 5. Using isinstance() Function
age = 20
weight = 66.89
print("check: isinstance(age, int) = ", isinstance(age, int))  # Output: True
print("check: isinstance(weight, int) = ", isinstance(weight, int))  # Output: False
print("check: isinstance(weight, float) = ", isinstance(weight, float))  # Output: True
