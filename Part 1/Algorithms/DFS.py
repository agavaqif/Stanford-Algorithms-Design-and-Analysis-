arr=[[1,2,5],[2,1,5,3],[3,2,4],[4,3,6],[5,1,2,6],[6,4,5],[7,8],[8,7]]
for i in arr:
    i.insert(0, "false")




def DFS(arr,start):
    result.append(start)
    arr[start-1][0]="true"
    for i in range(2,len(arr[start-1])):
        j=arr[start-1][i]
        if arr[j-1][0]=="false":
             DFS(arr,arr[j-1][1])
    return result







result=[]
print(DFS(arr,2))