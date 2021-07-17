def DFS(graph,start,visited):
    visited.append(start)
    print(start)
    t = graph[start]
    for i in t:
        if i not in visited:
            DFS(graph,i,visited)
    
#    stack = []
#
#    stack.append(start)
#    while stack:
#        print(stack[-1])
#        visited.append(stack[-1])
#        connected = graph[stack[-1]]
#        for i in connected:
#            if i not in visited:
#                DFS(graph,i,visited)
#        stack.pop()
            
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

visited = []
DFS(graph,"A",visited)


            



    
    
