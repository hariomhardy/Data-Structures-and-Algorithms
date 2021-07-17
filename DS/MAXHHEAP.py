def buildHeap(l):
    t = len(l)
    for i in range(1,t):
        if l[i] > l[i//2]:
            l[i],l[i//2] = l[i//2],l[i]
            Heapify(l,i)
    print(l)

def Heapify(l,i):
    h = i//2
    if l[h] > l[h//2] :
        l[h],l[h//2] = l[h//2],l[h]
        Heapify(l,h)



#n = int(input())
l = [5,7,12,22,1,6,3,28,29,8]
buildHeap(l)
