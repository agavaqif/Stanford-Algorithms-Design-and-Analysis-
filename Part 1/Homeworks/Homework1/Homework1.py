
array=[]
for value in open("IntegerArray.txt","r").readlines():
    array.append(int(value))

def divide(arr,c):
    if len(arr)<2:
        return arr
    firsthalf=divide(arr[:len(arr)//2],c)
    secondhalf=divide(arr[len(arr)//2:],c)
    return merge(firsthalf,secondhalf,c)

def merge(firsthalf,secondhalf,c):
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
            num=len(firsthalf)-i
            c[0]+=num
    if j<len(secondhalf):
        for j in range(j, len(secondhalf)):
            result.append(secondhalf[j])
    else:
        for i in range(i, len(firsthalf)):
            result.append(firsthalf[i])

    return result

def inversion_counter(arr):
    count_inversion=[0]
    divide(arr,count_inversion)
    return  count_inversion[0]

print(inversion_counter(array))