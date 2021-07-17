##### Take size of Tree of 4*n+1
import math

def prime(a):
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 0
    return 1

def build(n,seg,start,end,index):
    if start == end:
        seg[index] = prime(n[start])
        return
    mid = (start+end)//2
    build(n,seg,start,mid,2*index+1)
    build(n,seg,mid+1,end,2*index+2)
    seg[index] = seg[2*index+1]+seg[2*index+2]

def query(seg,l,r,start,end,index):
    if r < start or l > end :
        return 0
    elif l <= start and r >= end :
        return seg[index]
    mid = (start+end)//2
    return query(seg,l,r,start,mid,2*index+1)+query(seg,l,r,mid+1,end,2*index+2)

def update(n,seg,start,end,value,index,pos):
    if start == end :
           
           h = prime(value)
           if h == seg[pos] :
               n[index] = value
               return 0
           
           elif h == 0 :
               n[index] = value
               seg[pos] = 0
               return -1

           elif h == 1 :
               n[index] = value
               seg[pos] = 1
               return 1

    mid = (start + end)//2
    if (start <= index) and (mid >= index) :
        t = update(n,seg,start,mid,value,index,2*pos+1)
        seg[pos] += t
        return t
                   
    if mid <= index and end >= index :
        t = update(n,seg,mid+1,end,value,index,2*pos+2)        
        seg[pos] += t
        return t           


N,Q =  map(int,input().split())
n = list(map(int,input().split()))
k = int(round(pow(2,math.ceil(math.log2(N)))))
seg = [-1 for i in range(2*k - 1)]
build(n,seg,0,N-1,0)
for _ in range(Q):
    i,x,y = map(int,input().split())
    if i == 1:
        print(query(seg,x-1,y-1,0,N-1,0))
    if i == 2 :
        update(n,seg,0,N-1,y,x-1,0)
        


        
