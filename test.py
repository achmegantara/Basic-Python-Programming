number = [5, 8, 1, 10, 20, 3, 2, 7, 16, 11]


def sortAscending(number):
    for i in range(len(number)):
        for j in range(0, len(number)-i-1):
            if(number[j] > number[j+1]):
                (number[j], number[j+1]) = (number[j+1], number[j])


sortAscending(number)
print(number)
