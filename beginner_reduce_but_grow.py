"""https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python"""
from functools import reduce

def grow(arr):
    return reduce(lambda x,y: x * y, arr)


print(grow([1, 2, 3, 4]))
