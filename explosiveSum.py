def exp_sum(goal):
    numbers = [1]
    for n in range(1, goal+1):
        numbers.append(0)
        for k in range(1,n+1):
            for t in [int(k*(3*k-1) / 2), int((-k)*(3*(-k)-1) / 2)]:
                if n >= t:
                    numbers[n] = numbers[n] + (-1)**(k+1)*numbers[n-t]
                else:
                    break
    return numbers[-1]


print(exp_sum(5))