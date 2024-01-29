def find_it(seq):
    for element in set(seq):
        if seq.count(element) % 2: return element
