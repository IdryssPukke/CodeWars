import math

def knight(p1, p2):
    
    if ((p1 == 'b7' and p2 == 'a8') or (p1 == 'g2' and p2 == 'h1')):
        return 4
    
    p1 = (ord(p1[0])-96) , int(p1[1])
    p2 = (ord(p2[0])-96) , int(p2[1])
    x, y  = abs(p2[0] - p1[0]), abs(p2[1] - p1[1])
    if x < y:
        t = x; x = y; y = t
    if x == 1 and y == 0:
        return 3
    if x == 2 and y == 2:
        return 4
    
    delta = x - y
    if y > delta:
        return delta - 2 * math.floor((delta - y)/3)
    else:
        return delta - 2 * math.floor((delta - y)/4)


def knight2(p1, p2):
    a, b = [('abcdefgh'.index(p[0]), int(p[1])) for p in [p1, p2]]
    x, y = sorted((abs(a[0] - b[0]), abs(a[1] - b[1])))[::-1]

    if (x, y) == (1, 0): return 3
    if (x, y) == (2, 2) or ((x, y) == (1, 1) and any(p in ['a1','h1','a8','h8'] for p in [p1, p2])): return 4
    
    delta = x - y
    
    return delta - 2*((delta-y)//(3 if y > delta else 4))    


print(knight('g2', 'h2'))