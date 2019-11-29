def factornumber(number):
    max = number+1
    for i in range(1,max):
        if number%i == 0:
            factor.append(i)

factor = []
bil = int(input("Masukkan sebuah bilangan : "))
factornumber(bil)
print(factor)
