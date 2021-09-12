number = [1, 6, 3, 20, 10, 7, 4, 5, 21]
temp = []


def bublesort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            # descending
            if array[j] < array[j+1]:
                # ascending
                # if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])


print(len(number))
print(number)
bublesort(number)
print(number)
;
# 0-8
sumitomo mitsui banking corporation