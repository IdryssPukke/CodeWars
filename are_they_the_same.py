#  https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
    
    
def comp(array1, array2):
    if None is array1 or None is array2: 
        return False
    return sorted(map(lambda x: x**2, array1)) == sorted(array2)
    
    
comp( [121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361])
	