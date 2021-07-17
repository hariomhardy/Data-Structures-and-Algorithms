def bellford(graph,Min,a):
    for i in graph:
        for j in graph[i]:
            x,y = j
            if Min[x-1] > Min[i-1] + y :
                Min[x-1] = Min[i-1] + y
    print(Min)
            



graph = { 1 :[(2,6),(3,5),(4,5)],
          2 :[(5,-1)],
          3 :[(2,-2),(5,1)],
          4 :[(3,-2),(6,-1)],
          5 :[(7,3)],
          6 :[(7,3)],
          7 :[]
    }
n = 7
Min = [99]*n
Min[0] = 0
for i in range(n-1):
    bellford(graph,Min,1)


# can not work for graph with negative cycle
