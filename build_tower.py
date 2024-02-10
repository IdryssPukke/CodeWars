"""https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python"""


def tower_builder(n_floors):
    result = []
    for floor in range(n_floors):
        result.append((n_floors - floor - 1) * " " + (floor * 2 + 1) * "*" + (n_floors - floor - 1) * " ")
    return result
        

def tower_builder1(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


print(tower_builder(2))