a = int(input())
b = bin(a).replace("0b", "")

b = [int(i) for i in str(b)]
for i in range(len(b)):
    for j in range(0, len(b)-i-1):
        # descending
        if b[j] < b[j+1]:
            # ascending
            # if b[j] > b[j+1]:
            (b[j], b[j+1]) = (b[j+1], b[j])

# my_lst_str = ''.join(map(str, my_lst))

newB = ''.join(map(str, b))
intB = int(newB, 2)
print(b)
print(newB)
print(intB)
