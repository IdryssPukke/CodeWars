"""https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/python"""

def reverse_words(text):
    return ' '.join([ x[::-1] for x in text.split(' ')])
