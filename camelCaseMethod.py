def camel_case(s):
    return ''.join(list(map(lambda x: x.capitalize(), s.split())))

print(camel_case("hello case"))