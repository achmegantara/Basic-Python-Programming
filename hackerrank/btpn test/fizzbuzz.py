# def getScore(word):
#     # Write your code here
#     newWord = list(word.lower())
#     score = 0
#     for x in range(0, len(newWord), 1):
#         if x is "a" or "e" or "i" or "o" or "u" or "v" or "x" or "s":
#             score += 1
#         elif x is "d" or "g" or "h" or "t":
#             score += 2
#         elif x is "c" or "f" or "j" or "k" or "l" or "n" or "r":
#             score += 4
#         elif x is "b" or "m" or "p":
#             score += 6
#         elif x is "w" or "y":
#             score += 8
#         elif x is "q" or "z":
#             score += 10
#         else:
#             score += 0
#     return score


# a = "Zoo"
# b = getScore(a)
# print(b)

word = "Zoos"
newWord = list(word.lower())
print(newWord)
for x in newWord:
    if x in "z":
        print("true")
    else:
        print("false")
