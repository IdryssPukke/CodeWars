def solution(pairs):
    sol = ''
    for key, value in pairs.items():
        sol += str(key) + ' = ' + str(value) + ','
    return sol[:-1]

print(solution({'a': 1, 'b': 2}))