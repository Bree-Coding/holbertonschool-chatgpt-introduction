#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ----------------------
    This function calculates the factorial of a non-negative integer `n` using recursion. 
    The factorial of a number `n` is the product of all positive integers less than or equal to `n`.
    Factorial is defined as: n! = n * (n-1) * (n-2) * ... * 1, and 0! = 1 by definition.
    
    Parameters:
    -----------
    n : int
        A non-negative integer for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input integer `n`. If `n` is 0, the function returns 1 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Main program logic
# Get the number from command-line arguments, calculate its factorial, and print the result.
f = factorial(int(sys.argv[1]))  # Convert the first argument to an integer and compute its factorial
print(f)  # Output the calculated factorial

