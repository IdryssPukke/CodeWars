""""https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python"""


def number(bus_stops):
    
    passangers = list(map(sum, zip(*bus_stops)))
    return passangers[0] - passangers[1]


def number2(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

number([[10,0],[3,5],[5,8]])

