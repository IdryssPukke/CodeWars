"""https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python"""


def filter_list(l):
    return list(filter(lambda x: isinstance(x, (int)), l))