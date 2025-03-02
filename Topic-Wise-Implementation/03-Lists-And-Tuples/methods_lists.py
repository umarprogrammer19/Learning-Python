# Methods in lists
lists = [1, 2, 3, 4, 5]

# 1. append it adds the value at the end of the lists
lists.append(6)
print(lists)  # [1, 2, 3, 4, 5, 6]

# 2. sort it sorts the lists in the ascending order and if i gaves the argument of reverse = True so it sorts in the descending order

a = [5, 7, 8, 2, 3, 1, 9, 10]
a.sort()
print(a)  # [1, 2, 3, 5, 7, 8, 9, 10]

a.sort(reverse=True)
print(a)  # [10, 9, 8, 7, 5, 3, 2, 1]

# 3. reverse() reverse the lists
lists.reverse()
print(lists)  # [6, 5, 4, 3, 2, 1]

# 4. remove() it removes the 1st given element of the list for example if there is umar two times in the lists ao it is removes 1st umar coming in the list
lists.remove(4)
print(lists)  # [6, 5, 3, 2, 1]

# 5. insert it is used for inserting any value at any index
lists.insert(5, 10)  # add 10 in 5th index
print(lists)  # [6, 5, 3, 2, 1, 10]

# 6. pop() it removes element from the given index in the list
lists.pop(2)
print(lists)  # [6, 5, 2, 1, 10]

# 7. clear() removes all element from the lists
lists.clear()
print(lists) # []