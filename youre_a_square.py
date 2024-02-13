"""https://www.codewars.com/kata/5a023c426975981341000014/train/python"""
import math


def is_square(n):
    return False if n < 0 else n == math.sqrt(n)**2    