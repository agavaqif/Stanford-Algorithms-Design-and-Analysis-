

arr=[[1,2],[2,3,4],[3,1],[4,5],[5,6],[6,4],[7,6,8],[8,9],[9,10],[10,7,11],[11]];




def Done(array,arr):
    for i in range(2,len(arr)):
        j=arr[i]
        if array[j-1][0]=="false":
            return False
    return True

def Cleaner(cleaner,cleaned):
    for i in cleaner:
        if i in cleaned:
            cleaned.remove(i)
    return cleaned

def DFS(arr,start,checked,stack):
    current_node=start-1
    arr[current_node][0] = "true"
    checked.append(start)
    print(start)
    if len(arr[current_node])<3:
        stack.append(start)
    else:
        for i in range(2,len(arr[current_node])):
            j=arr[current_node][i]
            if arr[j-1][0]=="true":
                checked.reverse()
                print(checked)
                print("array",arr)
                for n in checked:
                        print("n is",n)
                        if Done(arr, arr[n - 1]):
                            stack.append(n)
                print("stack is",stack)
                Cleaner(stack,checked)
            else:
                DFS(arr,j,checked,stack)
    return stack




def Kosaraju(arr,start):
    check_list=[]
    for i in arr:
        check_list.append(i[0])
        i.insert(0, "false")
    print(arr)
    stack=[]
    checked=[]
    print(DFS(arr,start,checked,stack))
    Cleaner(stack,check_list)




Kosaraju(arr,9)
# arr is n arr[n-1]
