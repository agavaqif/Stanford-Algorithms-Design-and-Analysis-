import  heapq

array=[]
for value in open("Median.txt","r").readlines():
    array.append(int(value))



def Median(array):
    sum = 0
    for i in range(1,len(array)+1):
        arr=array[:i]
        heapq.heapify(arr)
        arr_len=len(arr)
        if arr_len%2==0:
            for i in range(0,int(arr_len/2)):
                median=heapq.heappop(arr)
            sum+=median
        else:
            for i in range(0,arr_len//2+1):
                median = heapq.heappop(arr)
            sum+= median
    return sum%10000


print(Median(array))

