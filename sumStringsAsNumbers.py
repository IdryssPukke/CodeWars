def sum_strings(x, y):
    
    x,y = map(str.strip, (x,y))
    
    if (x == '0' and y =='0') or (x == '' and y == ''):
        return "0"
    
    length = max(len(x), len(y))
    x, y = x.zfill(length)[::-1], y.zfill(length)[::-1]
    
    result = []
    carryover = 0
    
    for i in range(length):
        carryover, res = str(int(x[i]) + int(y[i]) + int(carryover)).zfill(2)
        result.append(res)
        if i == length - 1:
            result.append(carryover)

    result = "".join(result[::-1]).lstrip("0")
    return result if result else "0"



def sum_strings1(x, y):
    l, res, carry = max(len(x), len(y)), "", 0
    x, y = x.zfill(l), y.zfill(l)
    for i in range(l-1, -1, -1):
        carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
        res += str(d)
    return ("1" * carry + res[::-1]).lstrip("0") or "0"


print(sum_strings1("1230", "456"))