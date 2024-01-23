from math import floor


def century(year):
    print(floor(year/100))
    return floor(year/100) + 1 if floor(year/100) != year/100 else floor(year/100)


def century2(year):
    return (year + 99) // 100

print(century2(1700))