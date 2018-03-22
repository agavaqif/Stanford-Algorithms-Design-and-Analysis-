from random import randrange
from random import choice

array=[[1,2,3],[2,1,3,4],[3,1,2,4],[4,2,3]]


def concator(dead,alive):
    for i in dead:
        if i!=dead[0] and i!=alive[0]:
            alive.append(i)
    return list(filter(lambda x: x!=dead[0],alive))

def replaceAll(arr,old,new):
    for i in arr:
        if i==old:
            arr[arr.index(i)]=new
    return arr




def minCut(arr):
    if len(arr)<3:
        return arr
    dead=choice(array)
    allowed_values = list(filter(lambda x: x!=dead[0],dead))
    random_edge=choice(allowed_values)
    for i in arr:
        if i[0]==random_edge:
            alive=i
            break
    con=concator(dead,list(alive))
    alive_index=arr.index(alive)
    arr[alive_index]=con
    arr.remove(dead)
    for i in arr:
        if i!=con:
            replaceAll(i,dead[0],alive[0])
    return minCut(arr)


a=minCut(array)

print(a)
