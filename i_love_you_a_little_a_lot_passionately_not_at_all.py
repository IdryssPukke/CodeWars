#  https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python

def how_much_i_love_you(nb_petals):
    return {1: "I love you", 2: "a little", 3: "a lot", 4: "passionately", 5: "madly", 0: "not at all"}[nb_petals % 6]