def find_uniq(arr):
    uniq_elements = {}
    for element in arr:
        if element not in uniq_elements.keys():
            uniq_elements[element] = 1
        else:
            uniq_elements[element] += 1

    return (list(uniq_elements.keys())[list(uniq_elements.values()).index(1)])


print(find_uniq([ 0, 0, 0.55, 0, 0 ]))