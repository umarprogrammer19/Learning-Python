# Print Numbers b/w 1 - 100
nums = 1
while nums <= 100:
    print(nums)
    nums += 1

# Print Numbers b/w 100 - 1
nums = 100
while nums >= 1:
    print(nums)
    nums -= 1

# print the multiplication of a table of number n
n = int(input("Please enter a number of table to print: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

# print the elements of the following list using loop
# [1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100]

nums_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(nums_list):
    print(nums_list[i])
    i += 1

# search for a number x from the tuple using loop
# (1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)

nums_list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = int(input("Please enter a number to find: "))
while i < len(nums_list):
    if x == nums_list[i]:
        print(f"{x} Found at index {i}")
        break
    i += 1

# continue skips the current iteration for example i want to print the odd number from 1-10
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
