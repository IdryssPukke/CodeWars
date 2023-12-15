def printer_error(s):
    return '{}/{}'.format([True if ord(element) > ord('m') else False for element in s].count(True), len(s))

def printer_error1(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
   

print(printer_error('saaaas'))