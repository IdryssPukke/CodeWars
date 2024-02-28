# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python


def high(x):
    words = list(map(lambda x: sum([ord(char) - 96 for char in x]), x.split(" ")))
    return x.split(" ")[words.index(max(words))]
    

def high2(x):
    return max(x.split(),key=lambda x: sum(ord(char) for char in x))

print(high2('man i need a taxi up to ubud'))