import sys

def MstMin(checker,l):
    min1 = 99999
    j = -1
    for i in range(len(checker)):
        if checker[i][0]< min1 and l[i] == False:
            min1 = checker[i][0]
            j = i
    l[j] = True
    return j+1
            
def MST(graph):
    k = len(graph)
    l = [False] * k
    
    mst = {i : []  for i in range(1,k+1)}
    max1 = sys.maxsize
    checker = [[max1,0] for _ in range(k-1)  ]
    checker.insert(0,[0,0])
    s = 1
    l[0] = True 
    
    for i in range(len(graph)-1):
        t = graph[s]
        for x,y in t:
            if checker[x-1][0] > min(checker[s-1][0]+y,checker[x-1][0]):
                checker[x-1][0] = min(checker[s-1][0]+y,checker[x-1][0])
                checker[x-1][1] = s

        j = MstMin(checker,l)
        mst[checker[j-1][1]].append(j)

        s = j

    print(mst)
        
graph = {1 : [(2,28),(6,10)],
         2 : [(1,28),(3,16),(7,14)],
         3 : [(2,16),(4,12)],
         4 : [(3,12),(7,18),(5,22)],
         5 : [(4,22),(7,24),(6,25)],
         6 : [(5,25),(1,10)],
         7 : [(2,14),(4,18),(5,24)]}

MST(graph)

