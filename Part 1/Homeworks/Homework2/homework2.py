from random import randrange
from functools import reduce


array=[]
for value in open("QuickSort.txt","r").readlines():
    array.append(int(value))



def summer(arr):
    return reduce((lambda x,y:x+y),(arr))

def quickSort(arr,count,p):
    if len(arr)<2:
        return arr
    left=[]
    right=[]
    if p==1:
        pivot=0
    elif p==2:
        pivot=len(arr)-1
    else:
        if len(arr)%2==0:
            pivot=int(len(arr)/2)-1
        else:
            pivot=int(len(arr)//2)
    count.append(len(arr)-1)
    for j in range(0,len(arr)):
        if j==pivot:
            continue
        if arr[j]<arr[pivot]:
            left.append(arr[j])
        else:
            right.append(arr[j])
    result=quickSort(left,count,p)+[arr[pivot]]+quickSort(right,count,p)
    return result


arr=[3,1,2,4,5]

def counter(p):
    count=[]
    quickSort(array,count,p)
    print(summer(count))

counter(1)
counter(2)
counter(3)



