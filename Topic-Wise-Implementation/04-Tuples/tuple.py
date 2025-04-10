# Same As List But It Is Immutable
tup = (1, 2, 3, 5)
print(tup[0])

# tup[0] = 9 # Not Valid

# If we need to create a tuple of one element inside we need to create this seperated with , like this tup = (1,) because the parentheseis also normally use in python so if we can write tup = (1) so it behaves as a number in python tup = (1,) it is compulsory

print(tup[1:3])  # (2,3) same as list

# Methods of tuples
# 1) index find the index of the given element
a = (1, 2, 4, 5, 6, 7, 8, 9, 2, 10, 2)
print(a.index(4))  # prints 2 because the index of 4 is 2 in this tuple

# 2) count this methods counts the number of elements found in the tuples
print(a.count(2)) # prints 3
