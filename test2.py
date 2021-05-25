import math
import os
import random
import re
import sys


def barisanBertopi(n, tinggi, nilai):
    count = []
    for i in range(n):
        if i == 0:
            count.append(0)
        elif i >= 1:
            if tinggi[i] > tinggi[i-1] or tinggi[i] == tinggi[i-1]:
                for x in range(i):
                    count.append(nilai[x])
    return sum(count)


n = int(input().strip())

H = list(map(int, input().rstrip().split()))

C = list(map(int, input().rstrip().split()))

result = barisanBertopi(n, H, C)

print(str(result) + '\n')
