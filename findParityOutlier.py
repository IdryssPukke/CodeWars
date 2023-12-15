def find_outlier(integers):
    wynik = list(map(lambda x: x % 2 == 0, integers))
    return integers[wynik.index(False)] if wynik.count(True) > wynik.count(False) else integers[wynik.index(True)]


def find_outlier2(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(sum(parity) == 1)]

print(find_outlier2([2, 4, 0, 100, 4, 11, 2602, 36]))