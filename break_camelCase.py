"""https://www.codewars.com/kata/5208f99aee097e6552000148/train/python"""


def solution(s):
    return ''.join([' ' + letter if letter.isupper() else letter for letter in s])