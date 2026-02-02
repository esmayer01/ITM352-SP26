# Handy library of mathematical functions
# Name: Ethan Mayer
# Date: Jan. 27, 2026

def midpoint(num1, num2):
    """Calculate the midpoint between two numbers."""
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    """Calculate the square root of a number"""
    if number < 0:
        return None
    return number ** 0.5

def exponent(base, exp, precision):
    """Calculate the exponentiation of a base to a given exponent"""
    result = base ** exp
    rounded_result = round(result, precision=2)
    return rounded_result

def max(num1, num2):
    # return the maximum of two numbers
    return num1 if num1 > num2 else num2

def min(num1, num2):
    # return the minimum of two numbers
    return num1 if num1 < num2 else num2

def absolute_value(number):
    """Return the absolute value of a number."""
    return number if number >= 0 else -number

def apply_function(x, y, func):
    """
    Applies a function to x and y and returns a formatted string.
    """
    result = func(x, y)
    return f"The function {func.__name__} {x}, {y} = {result}"