import sys
array=[[1,[2,4],[8,8]],[2,[1,4],[3,8],[8,11]],[3,[2,8],[4,7],[6,4],[9,2]],[4,[3,7],[5,9],[6,14]],[5,[4,9],[6,10]],[6,[3,4],[4,14],[5,10],[7,2]],
       [7,[6,2],[8,1],[9,6]],[8,[1,8],[2,11],[7,1],[9,7]],[9,[3,2],[7,6],[8,7]]]


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












Dijakartas(array,9)

