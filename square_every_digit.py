def square_digits(num):
    return int(''.join([str(int(element) * int(element)) for element in str(num)]))




print(square_digits(765))