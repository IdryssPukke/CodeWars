"""https://www.codewars.com/kata/523f5d21c841566fde000009"""

def array_diff(a, b):
    """
    Your goal in this kata is to implement a difference function, 
    which subtracts one list from another and returns the result.

    Args:
        a (list): list with integers
        b (list): list with integers

    Returns:
        list: list with integers
    """
    return list(filter( lambda x: x not in b , a))

print(array_diff([1, 2, 3], [2]))
