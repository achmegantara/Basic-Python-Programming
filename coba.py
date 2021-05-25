# a = "achmad"
# li = []
# for i in range(len(a)):
#     li.append(a[i])

# print(li)

# a = [1, 2, 3, 4, 5]
# b = a[3:]

# print(b)1

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1)
       for k in range(Z + 1) if i + j + k == N and k != 0]
print(ans)
print(len(ans))
