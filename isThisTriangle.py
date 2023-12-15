def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: return False
    s = (a + b + c) / 2
    return False if (s-a)*(s-b)*(s-c) <= 0 else True

def is_triangle2(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

print(is_triangle(1, 2 , 2))