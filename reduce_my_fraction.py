# https://www.codewars.com/kata/576400f2f716ca816d001614/train/python
import math


def reduce_fraction(fraction):
    return [fraction[0]/math.gcd(fraction[0], fraction[1]),fraction[1]/math.gcd(fraction[0], fraction[1])]
