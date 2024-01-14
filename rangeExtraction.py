def solution(args):
    final = ''
    span = 0
    args += [0] 
    for x in range(len(args)-1):
        if abs(args[x+1] - args[x]) == 1:
            span += 1
        elif span > 1:
            final += str(args[x-span]) + '-' + str(args[x]) + ','
            span = 0
        elif span == 1:
            final += str(args[x-1]) + ',' + str(args[x]) + ','
            span = 0
        else:
            final += str(args[x]) + ','
            span = 0
    return final[:-1]
    
    
print(solution([-3,-2,-1,2,10,15,16,18,19,20]))