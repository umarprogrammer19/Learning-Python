print("Hello World")

# For Storing Values 
name = "Hafiz Muhammad Umar Farooq"
age = 16
isAlive = True

print("My Name is:", name)
print("My Age is:", age)

# For Types Of Variables
print(type(name))
print(type(age))
print(type(isAlive))

# Opearators
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(int(a / b))
print(a % b)
# Greater 
print(a > b)
# Less Then
print(a < b)
print(a < b)  # False
print(not (a < b))  # True
print(a == b)
print(a != b)

a += 10
print(a)  # 20
a -= 10
print(a)  # 10
a *= 10
print(a)  # 100
a /= 10
print(a)  # 10.0
print(int(a))  # 10

c = True
d = False
print(c and d)
print(c or d)

e = 20
f = "40"
# print(e + f) # Type Error Because We Cant Concatenate String And Integer At a Time;
print(
    e + int(f)
)  # This will returns 60 because now f is converted into integer with the help of int method

# For Taking Input From User
input("Enter Your Name:")

# First Class The End Now Practice
