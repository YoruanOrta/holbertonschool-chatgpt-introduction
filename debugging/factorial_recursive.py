#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    Function Description:
    The factorial of a number `n` is the product of all positive integers less than 
    or equal to `n`. It is defined as:
      n! = n × (n-1) × (n-2) × ... × 1
    For `n = 0`, the factorial is defined as 1.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number `n`.
    """
    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n-1)

# Ensure the user provides a command-line argument
if len(sys.argv) < 2:
    print("Usage: ./factorial_recursive.py <number>")
    sys.exit(1)

# Calculate and print the factorial of the input number
try:
    num = int(sys.argv[1])
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
        sys.exit(1)
    f = factorial(num)
    print(f)
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)
