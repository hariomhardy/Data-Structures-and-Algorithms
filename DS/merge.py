def sort1(n,l,r):
    if l < r :
        mid = (l+r)//2
        sort1(n,l,mid)
        sort1(n,mid+1,r)
        merge(n,l,mid,r)


def merge(n,l,mid,r):
    i = l
    j = mid + 1
    t = [] 
    while i < mid + 1 and j < r+1 :
        if n[i] < n[j] :
            t.append(n[i])
            i += 1
        else :
            t.append(n[j])
            j += 1
            
    while i < mid + 1 :
        t.append(n[i])
        i += 1
    while j < r+1 :
        t.append(n[j])
        j += 1

    n[l:r+1] = t
    
    

n= [7,5,12,21,3,2,1,56,98,89]
sort1(n,0,len(n)-1)
print(n)
