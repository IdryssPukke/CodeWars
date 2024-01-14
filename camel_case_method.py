"""https://www.codewars.com/kata/587731fda577b3d1b0001196"""


def camel_case(s):
    """
    A function that converts a string to camelCase, that is, 
    all words must have their first letter capitalized and spaces must be removed.

    Args:
        s (string): input string

    Returns:
        string: output string
    """
    return ''.join(list(map(lambda x: x.capitalize(), s.split())))

print(camel_case("hello case"))
