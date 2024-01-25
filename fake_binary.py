"""https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python"""


def fake_bin(x):
    return ''.join(map(lambda x: '0' if int(x) < 5 else '1', x))

