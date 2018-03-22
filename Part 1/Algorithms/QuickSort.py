#Quicksort pivot is index no 0
def quicksort(arr):
    if len(arr)<2:
        return arr
    i=1
    for j in range(1,len(arr)):
        if arr[j]<arr[0]:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
    arr[0],arr[i-1]=arr[i-1],arr[0]
    result=quicksort(arr[:(i - 1)])+[arr[i-1]]+quicksort(arr[i:])
    return result



#quicksort for general pivot.Random range used as example
from random import randrange
def quickSort(arr):
    if len(arr)<2:
        return arr
    pivot=len(arr)-1
    left=[]
    right=[]
    for j in range(0,len(arr)):
        if j==pivot:
            continue
        if arr[j]<arr[pivot]:
            left.append(arr[j])
        else:
            right.append(arr[j])
    result=quickSort(left)+[arr[pivot]]+quickSort(right)
    return result




arr=[6,4,2,5,12,7,22]
print(quickSort(arr))
print(quicksort(arr))