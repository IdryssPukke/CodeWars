def order_weight(strng): 
    return ' '.join(sorted(sorted(strng.split()), key = sortList))

def sortList(num):
    return sum(map(int, str(num)))

def order_weight2(strng): 
    return ' '.join(sorted(sorted(strng.split()), key = lambda x: sum(map(int, str(x)))))

print(order_weight2("2000 10003 1234000 44444444 9999 11 11 22 123"))