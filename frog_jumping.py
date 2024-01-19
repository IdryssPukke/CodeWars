def solution(a):
    iterator, index, indexes = 0, 0, []
    while True:
        if index > len(a)-1 or index < 0:
            return iterator
        elif index in indexes:
            return -1
        indexes.append(index)
        index += a[index]
        iterator +=1
        
    

print(solution([1, 2, 1, 5]))
        