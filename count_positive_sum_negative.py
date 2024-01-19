def count_positives_sum_negatives(arr):
    return [len(list(filter(lambda x: x > 0, arr))), sum(filter(lambda x: x < 0, arr))] if arr else []
    
    
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))