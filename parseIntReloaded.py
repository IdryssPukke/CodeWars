wordReps = {
    "ninety": 90,    "nineteen": 19,    "nine": 9,
    "eighty": 80,    "eighteen": 18,    "eight": 8,
    "seventy": 70,   "seventeen": 17,   "seven": 7,
    "sixty": 60,     "sixteen": 16,     "six": 6,
    "fifty": 50,     "fifteen": 15,     "five": 5,
    "forty": 40,     "fourteen": 14,    "four": 4,
    "thirty": 30,    "thirteen": 13,    "three": 3,
    "twenty": 20,    "twelve": 12,      "two": 2,
    "ten": 10,       "eleven": 11,      "one": 1,
    "zero": 0,
}

def parse_int(string):
    strArr = string.lower().replace('-'," ").split(" ")
    strArr = list(filter(lambda x: x != 'and', strArr))

    current, result = 0, 0
    for word in strArr:
        match word:
            case "million":
                result += current * 1000000
                current = 0
            case "thousand":
                result += current * 1000
                current = 0
            case "hundred":
                current *=  100
            case _:
                current += wordReps[word]

    return result + current

print(parse_int('six hundred sixty-six thousand six hundred sixty-six'))