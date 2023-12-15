def move_zeros(lst):
    zeros = list(filter(lambda x: x == 0, lst))
    lst = list(filter(lambda x: x != 0, lst))
    return lst + zeros

def move_zeros2(lst):
    lst.sort(key=lambda x: x == 0)
    return lst

print(move_zeros2([1, 0, 1, 2, 0, 1, 3]))