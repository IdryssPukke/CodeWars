"""https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python"""


def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(letter) <2 else ')' for letter in word.lower()])
        