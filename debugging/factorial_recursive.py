#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) < 2:
    print("Usage: ./factorial_recursive.py <number>")
    sys.exit(1)  # Exit the program if no arguments are provided

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
