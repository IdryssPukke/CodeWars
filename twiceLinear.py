def dbl_linear(n):
    list, x, y = [1], 0, 0
    for _ in range(n):
        nextY, nextZ = 2 * list[x] + 1, 3 * list[y] + 1 
        
        if nextY <= nextZ:
            list.append(nextY)
            x += 1
            if nextY == nextZ:
                y += 1
        else:
            list.append(nextZ)
            y += 1
            
    return list[n]


def dbl_linear1(n):
  num_list = [1]
  for i in num_list:
    num_list.append((i * 2) + 1)
    num_list.append((i * 3) + 1)
    if len(num_list) > n *10:
      break
  return sorted(list(set(num_list)))[n]

print(dbl_linear1(50))