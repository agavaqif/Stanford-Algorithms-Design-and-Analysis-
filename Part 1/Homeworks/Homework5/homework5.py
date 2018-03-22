import sys
with open("dijkstraData.txt") as f:
    content = f.readlines()
content = [x.strip().split() for x in content]



array=[]

for i in content:
    temp=[]
    for j in i:
        if "," in j:
            q = list(map(int, j.split(",")))
            temp.append(q)
        else:
            temp.append(int(j))
    array.append(temp)


def Printer(distance):
    for i in distance:
        print(distance.index(i)+1,i)

def Dijakartas(arr,start):
    visited=[False]*len(arr)
    distance=[sys.maxsize]*len(arr)
    x=[start]
    visited[start-1]=True
    distance[start-1]=0
    while len(x)<len(arr):
        temp = sys.maxsize
        for j in x:
            current_node = j
            for i in arr[j-1]:
                if type(i) is list and visited[i[0] - 1] == False:
                    length_i = distance[current_node - 1] + i[1]
                    if length_i < temp:
                        temp = length_i
                        next_node = i[0]
        x.append(next_node)
        distance[next_node - 1] = temp
        visited[next_node-1]=True
    Printer(distance)

Dijakartas(array,1)


