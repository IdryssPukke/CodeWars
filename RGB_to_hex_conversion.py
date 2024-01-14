"""https://www.codewars.com/kata/513e08acc600c94f01000001"""


def rgb(r, g, b):
    """
    The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
    Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

    Args:
        r (Int): red
        g (Int): green
        b (Int): blue

    Returns:
        _type_: hex color
    """
    result = ""
    for element in r, g, b:
        if element < 0:
            element = 0
        elif element > 255:
            element = 255
        convert = "{0:X}".format(element)
        result += "0" + convert if len(convert) == 1 else convert

    return result


def rgb1(r, g, b):
    """ """
    rounded = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rounded(r), rounded(g), rounded(b))


print(rgb1(254, 253, 252))
