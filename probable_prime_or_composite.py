"""https://www.codewars.com/kata/5742e725f81ca04d64000c11/train/python"""


from random import randint

def prime_or_composite(n, k=5):
    
    if n < 2: return "Composite"
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: 
            if(n == p):
                return "Probable Prime"
            else:
                return "Composite"
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d>>1
    for _ in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for _ in range(1, s):
            x = (x * x) % n
            if x == 1: return "Composite"
            if x == n-1: break
        else: return "Composite"
    return "Probable Prime"
