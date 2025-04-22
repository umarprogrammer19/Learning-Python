# WAF to print the length of a list list is a parameter
def length_of_list(list):
    print(len(list))


length_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# WAF to print the element of a list in a single line list is a parameter
def print_list_element_in_a_single_line(list):
    print(" ".join(map(str, list)))


print_list_element_in_a_single_line([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# WAF to find the factorial of n (n is a parameter)
def find_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(find_factorial(5))


# WAF to convert USD into PKR
def converter(curr_usd):
    pkr_value = curr_usd * 280
    return pkr_value


print(converter(100))


# WAF to check the number is even or odd
def check_even_or_odd(n):
    if isinstance(n, int):
        if n % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Please Enter a number"


print(check_even_or_odd(12))
