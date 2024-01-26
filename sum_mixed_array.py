"""https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python"""


def sum_mix(arr):
    result = 0
    for x in arr:
        result += int(x) 
    return result

def sum_mix1(arr):
    return sum(map(int, arr))

print(sum_mix([9, 3, '7', '3']))