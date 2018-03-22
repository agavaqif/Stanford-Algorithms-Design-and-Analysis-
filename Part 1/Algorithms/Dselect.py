def divide(arr):
    if len(arr)<2:
        return arr
    firsthalf=divide(arr[:len(arr)//2])
    secondhalf=divide(arr[len(arr)//2:])

    return merge(firsthalf,secondhalf)

def merge(firsthalf,secondhalf):
    result=[]
    k = 0
    i = 0
    j = 0
    while i < len(firsthalf) and j < len(secondhalf):
        if firsthalf[i] <= secondhalf[j]:
            result.append(firsthalf[i])
            i = i + 1
        else:
            result.append(secondhalf[j])
            j = j + 1

    if j<len(secondhalf):
        for j in range(j, len(secondhalf)):
            result.append(secondhalf[j])
    else:
        for i in range(i, len(firsthalf)):
            result.append(firsthalf[i])

    return result

def medianFinder(arr):
    if len(arr) % 2 == 0:
        return arr[int(len(arr) / 2) - 1]
    else:
        return arr[int(len(arr) // 2)]


def medianofMedian(arr):
    result=[]
    for i in range(0,len(arr),5):
        temp=divide(arr[i:i+5])
        result.append(medianFinder(temp))
    if len(result)<6:
        return medianFinder(result)
    else:
        return medianofMedian(result)


def partiation(arr,p):
    left=[]
    right=[]
    for i in arr:
        if i<p:
            left.append(i)
        elif i>p:
            right.append(i)
    return left+[p]+right

def Dselect(arr,m):

    pivot=medianofMedian(arr)
    index_pivot=partiation(arr,pivot).index(pivot)
    if m==index_pivot:
        return pivot
    elif m<index_pivot:
        return Dselect(partiation(arr,pivot)[:index_pivot],m)
    else:
        return Dselect(partiation(arr,pivot)[index_pivot+1:],m-index_pivot)



arr=[1,5,8,3,54,23,4,32,18,19,22,120,9,27,36,76,65,67,24,32,43,46,13, 17, 20, 15, 66, 35, 16, 44, 30, 31, 34, 132, 21, 36, 39, 48, 88, 77, 79, 36, 44, 55, 58]


