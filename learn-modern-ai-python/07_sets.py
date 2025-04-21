# Author: Arif Kasim Rozani - (Team Operation Badar)

# The Set Data Type
# A set is an unordered, unindexed, mutable collection with no duplicate elements.

# Creating Sets
my_set = {123, 452, 5, 6}
my_set2 = set([123, 452, 5, 6])
unknown = {}  # {} creates an empty dictionary, not a set
empty_set = set()  # Creates an empty set

print("my_set            = ", my_set)
print("my_set2           = ", my_set2)
print("type(my_set)      = ", type(my_set))
print("type(my_set2)     = ", type(my_set2))
print("type(unknown)     = ", type(unknown))  # This will print <class 'dict'>
print("type(empty_set)   = ", type(empty_set))  # This will print <class 'set'>
print("my_set == my_set2 = ", my_set == my_set2)

# my_set            =  {123, 452, 5, 6}
# my_set2           =  {123, 452, 5, 6}
# type(my_set)      =  <class 'set'>
# type(my_set2)     =  <class 'set'>
# type(unknown)     =  <class 'dict'>
# type(empty_set)   =  <class 'set'>
# my_set == my_set2 =  True

# 1. Sets can only store immutable objects like numbers, strings, and tuples
# Let's try storing a list in a set, which will raise a TypeError
try:
    my_set = {[123, 452, 5, 6]}  # This will raise a TypeError because lists are mutable
    print(my_set)
except TypeError as e:
    print(f"Error: {e}")

# 2. A set can hold multiple data types at once
multi_type_set = {7, 9.0, False, True, "Hello! World", (1, 5, 9, "hi")}
print(multi_type_set)  # Output: {False, True, 7, 9.0, 'Hello! World', (1, 5, 9, 'hi')}

# 3. Sets are unordered, so the elements might not be in the order they were added
set2 = {"Java", "Python", "JavaScript", "java"}
print(set2)  # Output: {'Python', 'Java', 'java', 'JavaScript'}

# 4. Sets are unchangeable (you cannot change an item directly), but you can add or remove items
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

try:
    my_set[0] = (
        10  # This will raise an error because sets do not support indexing or item assignment
    )
except TypeError as e:
    print("Error:", e)

# 5. Removing items from a set
my_set.remove(3)
my_set.remove(4)
print("After remove:", my_set)  # Output: {1, 2, 5}

# Adding an item
my_set.add(6)
print("After add:", my_set)  # Output: {1, 2, 5, 6}

# Discarding an element (if not present, it does nothing)
my_set.discard(2)
my_set.discard(
    10
)  # Will not raise an error as discard does nothing if the element is not found
print("After discard:", my_set)  # Output: {1, 5, 6}

# 6. Using difference_update to remove multiple elements from a set
my_set.difference_update({1, 5})
print("After difference_update:", my_set)  # Output: {6}

# 7. Set Union using the union() method or | operator
set1 = {1, 2, 3, 5}
set2 = {1, 5, 6, 7}
union_set = set1.union(set2)
print("Union (using union method):", union_set)  # Output: {1, 2, 3, 5, 6, 7}

# Union using | operator
union_set = set1 | set2
print("Union (using | operator):", union_set)  # Output: {1, 2, 3, 5, 6, 7}

# 8. Set Intersection using intersection() method or & operator
intersection_set = set1.intersection(set2)
print("Intersection (using intersection method):", intersection_set)  # Output: {1, 5}

# 9. Set Symmetric Difference using symmetric_difference() method or ^ operator
symmetric_difference_set = set1.symmetric_difference(set2)
print(
    "Symmetric Difference (using symmetric_difference method):",
    symmetric_difference_set,
)  # Output: {2, 3, 6, 7}

# 10. Set Difference using difference() method or - operator
difference_set = set1.difference(set2)
print("Difference (using difference method):", difference_set)  # Output: {2, 3}

# 11. Pop a random element from the set
popped_item = my_set.pop()
print("Popped item:", popped_item)
print("Set after pop:", my_set)

# Frozensets
# Frozenset is an immutable version of a set, meaning you can't modify it after creation
frozenset1 = frozenset([1, 2, 3, 4])
frozenset2 = frozenset([3, 4, 5, 6])

print(f"frozenset1: {frozenset1}")
print(f"frozenset2: {frozenset2}")

# Methods that work with frozensets (since they are immutable)
difference_frozenset = frozenset1.difference(frozenset2)
print(
    f"difference() with frozensets: {difference_frozenset}"
)  # Output: frozenset({1, 2})

intersection_frozenset = frozenset1.intersection(frozenset2)
print(
    f"intersection() with frozensets: {intersection_frozenset}"
)  # Output: frozenset({3, 4})

union_frozenset = frozenset1.union(frozenset2)
print(
    f"union() with frozensets: {union_frozenset}"
)  # Output: frozenset({1, 2, 3, 4, 5, 6})

# Frozensets are hashable and can be used as dictionary keys
my_dict = {frozenset1: "Set1", frozenset2: "Set2"}
print(f"Dictionary with frozenset keys: {my_dict}")
