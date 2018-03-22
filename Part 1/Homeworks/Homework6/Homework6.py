array=[]
for value in open("values.txt","r").readlines():
    array.append(int(value))

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

def IntervalSummer(arr,interval):
    c_array=[]
    start=0
    end=len(arr)-1
    while start<end:
        if arr[start]+arr[end]<interval[0]:
            start+=1
        elif arr[start]+arr[end]>interval[1]:
            end-=1
        else:
            c_array.append([arr[start],arr[end]])
            t_s=start
            t_e=end
            temp_start=start+1
            temp_end=end-1
            while True:
                if arr[temp_start]+arr[t_e]>interval[1]:
                    start+=1
                    break
                elif temp_start<end:
                    if arr[temp_start]!=arr[t_e]:
                        c_array.append([arr[temp_start],arr[t_e]])
                    temp_start += 1
                else:
                    break
            while True:
                if arr[temp_end]+arr[t_s]<interval[0]:
                    end-=1
                    break
                elif temp_end>t_s:
                    if arr[t_s]!=arr[temp_end]:
                        c_array.append([arr[t_s],arr[temp_end]])
                    temp_end -= 1
                else:
                    break

    return c_array

arr=divide(array)
interval=[-10000,10000]
res=IntervalSummer(arr,interval)
result=[]
for i in res:
    a=i[0]+i[1]
    if a not in result:
        result.append(a)
print(len(result))
