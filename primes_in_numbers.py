def prime_factors(n):
    k, dict = 2, {}
    
    while n > 1:
        if n % k == 0:
            dict[k] = dict.get(k, 0) + 1
            n /= k
        else:
            k += 1
    return ''.join(["({}**{})".format(key, value) if value > 1 else "({})".format(key) for key, value in dict.items()])


print(prime_factors(86240))