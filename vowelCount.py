def get_count(sentence):
    return sum(list(map(lambda x: sentence.count(x),['a', 'e', 'i', 'o', 'u'])))


def getCount(s):
    return sum(c in 'aeiou' for c in s)

print(get_count("Incorrect answer for aeiou"))