def factornumber(number):
    for i in range(1, (number+1)):
        if number % i == 0:
            factor1.append(i)


def factornumber2(number):
    for i in range(1, (number+1)):
        if number % i == 0:
            factor2.append(i)


# input bilangan
bil = int(input("Masukkan bilangan 1 : "))
bil2 = int(input("Masukkan bilangan 2 : "))

# mencari faktor bilangan
factor1 = []
factor2 = []
factornumber(bil)
factornumber2(bil2)

# mencari fpb
temp = []
for i in range(0, len(factor1)):
    for j in range(0, len(factor2)):
        if factor1[i] == factor2[j]:
            temp.append(factor1[i])

fpb = max(temp)
print("Maka nilai fpb dari bilangan {0} dan {1} adalah {2}".format(
    bil, bil2, fpb))
print(temp)
