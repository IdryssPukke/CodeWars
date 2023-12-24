def get_pins(observed):
    combination = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['8', '0'],
    }
    if len(observed) == 1:
        return combination[observed]
    else:
        return [a + b for a in combination[observed[0]] for b in get_pins(observed[1:])]


print(get_pins('11'))