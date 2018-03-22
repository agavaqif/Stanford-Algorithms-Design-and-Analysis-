import queue



#First value of array is node number rest is edges
arr=[[1,2,5],[2,1,5,3],[3,2,4],[4,3,6],[5,1,2,6],[6,4,5],[7,8],[8,7]]

def BFS(arr,start):
    for i in arr:
        i.insert(0,"false")
    q=queue.Queue()
    result=[]
    q.put(start)
    arr[start-1][0]="true"
    while not q.empty():
        explored=q.get()
        result.append(explored)
        for i in range(2,len(arr[explored-1])):
            j=arr[explored-1][i]
            if arr[j-1][0]=="false":
                arr[j-1][0] ="true"
                q.put(arr[explored-1][i])

    print(result)







BFS(arr,2)