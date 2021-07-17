def bfs(graph,start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        connected = graph[node]

        if node not in visited:
            print(node)
            visited.append(node)
        

        for i in connected:
            if i not in visited:
                print(i)
                queue.append(i)
                visited.append(i)

def BFS(graph,start):
    queue = [start]
    visited = {}
    Bfs = []
    while queue:
        t = queue.pop(0)
        if t not in visited:
            visited[t] = True
            Bfs.append(t)
            for i in graph[t]:
                queue.append(i)
    print(Bfs)


graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

bfs(graph,"A")
BFS(graph,"A")



#n = int(input()) #no. of vertices
#e = int(input()) 
#graph = {}
#for _ in range(n):
#    graph[_ + 1] = []   

#for _ in range(e):
#    x,y = map(int,input().split())
#    graph[x].append(y)


