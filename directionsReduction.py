opposites = { "NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST" }

def dir_reduc(arr):
    
    result = [] 
    for i in range(0,len(arr)): 
        
        if not result: 
            result.append(arr[i]) 
            
        elif result[-1] != opposites[arr[i]]: 
            result.append(arr[i]) 
            
        else: 
            result.pop() 
            
    return result


def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    print(dir2)
    dir3 = dir2.split()
    print(dir3)
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3


print(dirReduc(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"]))