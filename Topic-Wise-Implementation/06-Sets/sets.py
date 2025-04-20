# set is a collection of unorderd items eact items in the set must be unique and immutable
nums = {1, 2, 3, 4, 5}
print(nums)  # {1, 2, 3, 4, 5}

nums = {1, 2, 2, 3, 4, 5, 5, 5}
print(nums)  # {1, 2, 3, 4, 5}

# you can also create a empty set but not like this a = {} this is dictionary
new_set = set()

# Methods of sets
# add add the values in the set
new_set.add(1)
new_set.add(2)
new_set.add(2)
new_set.add(3)

print(new_set)  # prints {1, 2, 3} because set values are unique

# remove delete the given value
new_set.remove(2)  # removes 2 from the set
print(new_set)  # {1, 3}

# clear (removes all elements from the sets)
new_set.clear()
print(new_set)  # set()

new_set.add(1)
new_set.add(2)
new_set.add(3)
new_set.add(4)
new_set.add(5)

# pop() delete random element from the sets
new_set.pop()
print(new_set) # returns all the element with removes any random value from the set
