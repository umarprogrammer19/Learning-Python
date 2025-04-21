# 1. Introduction to Control Flow and Decision Making in Python

# Comparison Operators
x: int = 10
y: int = 20

print("x == y = ", x == y)  # False
print("x != y = ", x != y)  # True
print("x > y  = ", x > y)  # False
print("x < y  = ", x < y)  # True
print("x >= y = ", x >= y)  # False
print("x <= y = ", x <= y)  # True

# Logical Operators
age: int = 25
is_student: bool = True

if age > 18 and is_student:
    print("You are eligible for a student discount.")

if age < 12 or age > 60:
    print("You qualify for a special discount.")

if not is_student:
    print("You are not a student.")

# 2. The if Statement
num: int = 10

if num > 0:
    print("The number is positive.")

# 3. The else Statement
num: int = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")

# 4. The elif Statement
num: int = 0

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 5. Nested if Statements
num: int = 10

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")

# 6. Practical Examples


# Example 1: Simple Calculator
def simple_calculator():
    operation: str = input("Enter the operation (+, -, *, /): ")
    num1: float = float(input("Enter the first number: "))
    num2: float = float(input("Enter the second number: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero."
    else:
        result = "Invalid operation."

    print("Result:", result)


simple_calculator()


# Example 2: Grading System
def grading_system(marks: float):
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade


marks = float(input("Enter marks: "))
grade = grading_system(marks)
print(f"The grade for {marks} marks is: {grade}")


# 7. Python match-case Statement
def check_status(code):
    match code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case _:
            print("Unknown Status")


check_status(200)  # Output: OK
check_status(404)  # Output: Not Found
check_status(500)  # Output: Unknown Status

# 8. Loops and Iteration

# The for Loop
fruits: list = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
word: str = "Python"
for letter in word:
    print(letter)

# for Loop with else
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
else:
    print("Loop completed successfully!")

# 9. The while Loop
count: int = 1
while count <= 5:
    print(count)
    count += 1

# 10. Controlling Loops with break and continue
# Break example
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue example
for i in range(5):
    if i == 3:
        continue
    print(i)

# 11. Nested Loops: Multiplication Table
for outer in range(1, 6):  # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 6):  # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()  # Add a blank line after each row

# 12. Practical Examples with Loops

# Example 1: Sum of Numbers from 1 to 100
total: int = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)

# Example 2: Finding Factors of a Number
num: int = 24
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num}: {factors}")
