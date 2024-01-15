"""https://www.codewars.com/kata/5970df092ef474680a0000c9"""


def alphabetized(s): 
    return ''.join(sorted([char for char in s if char.isalpha()], key=str.lower))


print(alphabetized("CodeWars can't Load Today"))
