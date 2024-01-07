def rgb(r, g, b):
    result = ''
    for element in r,g,b:
        if element< 0: element = 0
        elif element > 255: element = 255
        hex = "{0:X}".format(element)
        result += "0" + hex if len(hex) == 1 else hex

    return result

def rgb1(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


print(rgb1(254,253,252))