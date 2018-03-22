from random import randint




def partiation(arr,p):
    left=[]
    right=[]
    for i in arr:
        if i<p:
            left.append(i)
        elif i>p:
            right.append(i)
    return left+[p]+right

def Rselect(arr,m):
    if len(arr)==1:
        return arr[0]
    random_pivot=arr[randint(0,len(arr))]
    partiated_array=partiation(arr, random_pivot)
    index = partiated_array.index(random_pivot)
    print("array is:",arr)
    print("pivot is:",random_pivot)
    print("partiated is",partiated_array)
    print("index is:",index)
    if m==index:
        return random_pivot
    elif m<index:
        print("samller is:",partiation(arr,random_pivot)[:index])
        return Rselect(partiation(arr,random_pivot)[:index],m)
    else:
        print("bigger is:",partiation(arr,random_pivot)[index+1:])
        return Rselect(partiation(arr,random_pivot)[index+1:],m-index)



arr=[1,5,8,3,54,23,4,32,18,19,22,120,9,27,36,76,65,67,24,32,43,46,13, 17, 20, 15, 66, 35, 16, 44, 30, 31, 34, 132, 21, 36, 39, 48, 88, 77, 79, 36, 44, 55, 58]

print(Rselect(arr,29))

