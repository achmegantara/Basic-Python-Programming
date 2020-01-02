bil = int(input("Masukkan sebuah bilangan : "))
prime = True

if bil == 1:
    print("Bilangan prima merupakan bilangan yang lebih dari 1")
else:
    for i in range(2,bil):
        if bil%i != 0:
            pass
        elif bil%i ==0:
            prime = False
            break
        
if prime == True:
    print("Merupakan bilangan prima")
elif prime == False:
    print("Bukan merupakan bilangan prima")