
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



result=divide([5,2,3,0,100,12,1112,12,54,2])

print(result)

