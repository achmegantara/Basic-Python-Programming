def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        print("Nilai key = ",key)
        j = i-1
        print("Nilai j = ",j)
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

number = [20,10,25,5,2,60]
insertionsort(number)
print(number)


# i dari 1 sampai panjang array
# 