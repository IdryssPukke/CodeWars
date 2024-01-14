"""https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2"""

def solution(pairs):
    """
    Complete the solution so that it takes the dict passed in 
    and generates a human readable string from its key/value pairs. 

    Args:
        pairs (dict): dictionary with values

    Returns:
        string: string from dictionary
    """
    sol = ''
    for key, value in pairs.items():
        sol += str(key) + ' = ' + str(value) + ','
    return sol[:-1]

print(solution({'a': 1, 'b': 2}))
