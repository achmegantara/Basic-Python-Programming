def getNextGap(gap):
    gap = (gap*10)/13
    if gap < 1:
        return 1
    return gap

def combSort(arr):
    n = len(arr)
    gap = n
    swapped = True
    
    while gap !=1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        
        for i in range(0, n-gap):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap],arr[i]
                swapped = True

arr = [12,11,13,5,6,7,1,20,14,2,3,50,32,49,27]
combSort(arr)
print(arr)



