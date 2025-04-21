# Exception Handling with try, except, else, and finally

# Importance of Exception Handling in Python:
# - Prevents program crashes
# - Graceful error recovery
# - Keeps code clean, readable, and maintainable
# - Manages resources like files and network connections

# Scenarios where Exception Handling is Crucial:
# - File operations
# - User input validation
# - Network operations
# - Mathematical operations

# The try Block
# The try block tests a block of code for errors. If an error occurs, the program jumps to the except block.

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except:
    print("An error occurred!")  # This will catch the error

# Output: An error occurred!

# The except Block
# The except block handles specific errors. You can specify the type of error to catch.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output: Cannot divide by zero!

# The else Block
# The else block executes if no errors occur in the try block.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful. Result: {result}")

# Output: Division successful. Result: 5.0

# The finally Block
# The finally block executes regardless of whether an error occurred or not. It's typically used for cleanup.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")

# Output:
# Cannot divide by zero!
# This will always execute.


# Putting It All Together
def divide_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.")


# Test cases
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "2")  # TypeError

# Output:
# Division successful. Result: 5.0
# Operation complete.
# Error: Cannot divide by zero!
# Operation complete.
# Error: Invalid input type. Numbers required.
# Operation complete.

# Exception Handling Example with Functions and Multiple Error Types
import random
from typing import List, Tuple


def generate_random_data(num_samples: int) -> List[Tuple[int, int]]:
    """Generates a list of random number pairs."""
    try:
        if not isinstance(num_samples, int) or num_samples <= 0:
            raise ValueError("Number of samples must be a positive integer.")
        data = [
            (random.randint(1, 100), random.randint(1, 100)) for _ in range(num_samples)
        ]
        return data
    except ValueError as ve:
        print(f"Error: {ve}")
        return []  # Return empty list on error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def calculate_ratios(data: List[Tuple[int, int]]) -> List[float]:
    """Calculates the ratio of the first number to the second in each pair."""
    ratios = []
    try:
        for pair in data:
            num1, num2 = pair
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            if not isinstance(num1, int) or not isinstance(num2, int):
                raise TypeError("Input data must be integers.")
            ratio = num1 / num2
            ratios.append(ratio)
        return ratios
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        return []
    except TypeError as te:
        print(f"Error: {te}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during ratio calculation: {e}")
        return []


def process_data(num_samples: int) -> List[float]:
    """Combines data generation and ratio calculation with comprehensive error handling."""
    data = generate_random_data(num_samples)
    if not data:
        return []
    ratios = calculate_ratios(data)
    return ratios


# Example usage with error handling
try:
    num_samples = 10
    results = process_data(num_samples)
    if results:
        print("Calculated ratios:", results)
    else:
        print("Data processing failed due to an error.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Example of invalid input
results = process_data(-5)
if not results:
    print("Negative number of samples, data processing failed.")

results = process_data("abc")
if not results:
    print("Invalid input type, data processing failed.")

# Output:
# Calculated ratios: [0.48, 2.3, 1.3870967741935485, 2.9285714285714284, 0.5945945945945946, 0.8, 16.25, 0.723404255319149, 4.142857142857143, 0.922077922077922]
# Error: Number of samples must be a positive integer.
# Negative number of samples, data processing failed.
# Error: Number of samples must be a positive integer.
# Invalid input type, data processing failed.

# User Input Error Handling Example
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")


# Raising Exceptions Manually
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")  # Raising an exception
    return a / b


try:
    print(divide(10, 2))  # Output: 5.0
    print(divide(5, 0))  # This will raise an exception
except ValueError as e:
    print(f"Error: {e}")

# Output:
# 5.0
# Error: Division by zero is not allowed!


# Custom Exception Handling
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""

    pass


def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"{n} is positive"


try:
    print(check_positive(-5))  # This will raise a custom exception
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}")

# Output:
# Custom Exception Caught: Negative numbers are not allowed!
