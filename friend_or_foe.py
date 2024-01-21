"""https://www.codewars.com/kata/55b42574ff091733d900002f/train/python"""

def friend(x):
    return list(filter(lambda x: len(x) == 4, x))

print(friend(["Ryan", "Kieran", "Mark"]))
