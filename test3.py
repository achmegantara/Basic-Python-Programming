import math
import os
import random
import re
import sys


def findTotalWays(N, S):
    newString = []
    for i in range(N):
        newString.append(S[i])
        if S[i] == "o":
            start = i
    usedWay = newString[start+1:]
    for x in usedWay:
        if x == ".":
            countJalan += 1
        elif x == "_":
            countJurang += 1


if __name__ == '__main__':
    N = int(input().strip())

    S = input()

    result = findTotalWays(N, S)

    print(str(result) + '\n')
