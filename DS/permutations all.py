def permutation(n,i,t):
    length = len(n)
    if length > i:
        for j in range(i,length):
            n[i],n[j] = n[j],n[i]
            permutation(n,i+1,t)
            n[i],n[j] = n[j],n[i]
    else:
        t.append("".join(n))
    
def nextPermutation(n):
    length  = len(n)
    for i in range(length-1,-1,-1):
        if int(n[i]) > int(n[i-1]):
            index = i-1
            break

    small = 10
    for i in range(index,length):
        if int(n[i]) < small:
            smallest = i
    n[index] , n[smallest] = n[smallest],n[index]
    temp = n[:index+1] + sorted(n[index+1:])
    return "".join(temp)


        

s = input()
t = []
permutation(list(s),0,t)
print(*t)
print(nextPermutation(list(s)))

