"""
https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
"""

def square_sum(numbers):
    """
    Complete the square sum function so that it squares each number passed into it and then sums the results together.

    Args:
        numbers (Array): Array of numbers

    Returns:
        Int: Sum of all numbers
    """
    return sum([x ** 2 for x in numbers])
