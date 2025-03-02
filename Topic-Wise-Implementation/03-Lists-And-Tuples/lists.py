# List is defined as the collection of multiple values of multiple data types
#         0   1   2   3   4   5   6
marks = [10, 20, 30, 40, 50, 60, 70]
# For printing Type
print(type(marks))  # list

# Print All Values in the list 
print(marks)

# Prints a single value by using index
print(marks[0])  # 10

# For finding the length 
print(len(marks))  # 7

# Changing of values from index is allowed in lists 
marks[6] = 80

print(marks) # prints 80 intead of 70 on index 6

print(marks[7]) # Gives IndexError: list index out of range


