n = int(input())
arr = list(map(int, input().split()))
arr = list(dict.fromkeys(arr))

for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] < arr[j+1]:
            (arr[j], arr[j+1]) = (arr[j+1], arr[j])

print(arr[1])
