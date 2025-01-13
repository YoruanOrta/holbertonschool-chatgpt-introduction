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
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input from command-line arguments
f = factorial(int(sys.argv[1]))
print(f)
