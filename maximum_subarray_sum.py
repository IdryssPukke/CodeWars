"""https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python"""

    
def max_sequence(items):
    iter_items = iter(items)
    try:
        temp_sum = next(iter_items)
    except StopIteration:
        temp_sum = 0
    max_sum = temp_sum
    for item in iter_items:
        temp_sum = max(temp_sum + item, item)
        max_sum = max(temp_sum, max_sum)
    return max(max_sum, 0)

print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))