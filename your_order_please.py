"""https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python"""


def order(sentence):
    result = {}
    for word in sentence.split():  
        for letter in word:
            if letter.isnumeric():
                result[letter] = word
  
    return ' '.join([result[x] for x in sorted(result)])


def order2(words):
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


print(order2("is2 Thi1s T4est 3a"))
