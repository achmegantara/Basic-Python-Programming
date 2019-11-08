import sys

A = [64,25,12,22,11]

for i in range(len(A)):
    min_idx = i
    #i=1
    for j in range(i+1,len(A)):
        # j = 2
        if A[min_idx] > A[j]:
            min_idx = j
    
    A[i],A[min_idx] = A[min_idx], A[i]
    

print(A)
            