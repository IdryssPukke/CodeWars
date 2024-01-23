def array(string):
    return ' '.join(string.split(',')[1:-1]) or None


print(array("1,2,3,4" ))