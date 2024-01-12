import numpy as np

def persistence(n):
    return 0 if n < 10 else persistence(np.prod([int(x) for x in str(n)]))+1

print(persistence(999))