def combination(l,i,r,c):
    if len(c) == r:
        print(c)

    elif i >= len(l):
        return
    
    else:
        combination(l,i+1,r,c+str(l[i]))
        combination(l,i+1,r,c)


l = [1,2,3,4]
combination(l,0,3,"")

# l = list(map(int,input().split()))
# r = int(input())
# combination(l,0,r,"")

