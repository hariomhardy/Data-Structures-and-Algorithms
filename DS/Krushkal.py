def third(l):
    return l[2]
        
def MST(graph,parent):
    mst = {i : []for i in range(1,8)}
    l = graph.copy()
    l.sort(key = third)
    for i in l :
        if union(i[0],i[1]) :
            mst[i[0]].append(i[1])
    print(mst)


def find(parent,i):
    if parent[i-1] == -1:
        return i
    else:
        return find(parent,parent[i])
        

def union(i,j):
    x = find(parent,i)
    y = find(parent,j)
    if x ==y:
        return False
    else:
        return True
            
        
    




graph = [ (1,2,28),(1,6,10),(3,2,16),(7,2,14),(4,3,12),
          (7,4,18),(5,4,22),
          (7,5,24),(6,5,25)]

print(graph)

parent = [-1]*7

MST(graph,parent)





