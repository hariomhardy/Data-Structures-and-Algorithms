def quicksort(arr,l,h):
    if l<h:
        pivot = partition(arr,l,h)
        quicksort(arr,l,pivot-1)
        quicksort(arr,pivot+1,h)


def partition(arr,l,h):
    pivot = l
    end = h
    while l < h:
        while l < end and arr[l] <= arr[pivot]:
            l += 1
        while h > 0 and arr[h] > arr[pivot]:
            h -= 1

        if l<h:
            arr[l] ,arr[h] = arr[h],arr[l]

    arr[pivot],arr[h] = arr[h],arr[pivot]
    return h


arr = list(map(int,input().split()))
quicksort(arr,0,len(arr)-1)
print(*arr)
    
