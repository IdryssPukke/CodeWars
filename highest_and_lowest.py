"""https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python"""

def high_and_low(numbers):
    num = list(map(lambda x: int(x), numbers.split(' ')))
    print(num)
    return "{} {}".format(str(max(num)), str(min(num)))
