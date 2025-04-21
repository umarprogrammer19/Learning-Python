# loops => Reapeat we can use loops when we want to repeat a code for example i want to print hello world 10 times so i have two options 1st i write print("Hello World") 10 times 2nd thing i use loop

for i in range(10):  # 10 is a stopping condition
    print("Hello World", i)

list = ["Ammar", "Subhan", "Hammad", "Ali", "Umar"]

for el in list:
    print(el)

# print the elements of the following list using For loop
# [1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in nums:
    print(val)

# search for a number x from the tuple using loop
# (1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)

nums_tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Please Enter a Number to find in the tuple: "))

for num in nums_tup:
    if num == x:
        print(f"{x} Found")
        break

for i in range(0, 101, 2): # 0 is a starting condition 101 is a stopping condition and 2 is a step that i increase i in every time loop runs
    print(i)
