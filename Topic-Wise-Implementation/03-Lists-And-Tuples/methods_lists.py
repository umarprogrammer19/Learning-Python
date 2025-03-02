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
