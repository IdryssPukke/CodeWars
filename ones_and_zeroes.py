"""https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python"""

def binary_array_to_number(arr):
    return int(''.join(map(str,arr)),2)


print(binary_array_to_number([0, 0, 1, 0]))