# when a function call it self repeatedly called recursion
def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)
    print("End Of Function")


show(2)


# WAF to find the factorial of n using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# WARF to calculate the sum of first n natural numbers
def calc_sum_of_n_natural_numbers(n):
    if n == 0:
        return 0
    return calc_sum_of_n_natural_numbers(n - 1) + n


print(calc_sum_of_n_natural_numbers(5))


# WARF to print all the element in the list hint use list and index as a parameter
def print_list(list, idx=0):
    if idx == len(list):
        return list
    print(list[idx])
    print_list(list, idx + 1)


print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
