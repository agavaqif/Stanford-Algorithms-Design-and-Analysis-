

def TwoSum(arr,target):
    d={}
    for i in arr:
        if target-i in d:
            return (i,target-i)
        else:
            d[i]=i
    return -1

arr=[8,6,12,4]
target=11

print(TwoSum(arr,target))