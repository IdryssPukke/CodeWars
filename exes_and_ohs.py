"""https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python"""


def xo(s):
    return True if s.lower().count('o') == s.lower().count('x') else False

print(xo('ooxx'))
