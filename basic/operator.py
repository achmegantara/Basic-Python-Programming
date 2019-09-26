#operator aritmatika, pembanding, penugasan
#operator logika, bitwise, ternary

a = int(input("Inputkan nilai a : "))
b = int(input("Inputkan nilai b : "))

c = a+b
d = a*b
e = a/b
f = a%b
g = a**b
print(c,d,e,f,g)

#operator penugasan
ab = int(input("Inputkan nilai ab : "))
ab += 2
print(ab)
ab -= 2
print(ab)
ab *= 2
print(ab)
ab /= 2
print(ab)
ab ** 2

#berapakah nilai ab sekarang?
print(ab)

#operator pembanding
# == , <, >, <=, >=, !=

#operator logika
benar = True
salah = False

hasil = benar and salah
print(hasil)
hasil2 = benar or salah
print(hasil2)
hasil3 = not benar
print(hasil3)

#operator ternary
# <nilai true> if kondisi else <nilai fase>
umur = int(input("Berapa umur kamu?"))
aku = "bocah" if umur < 10 else "dewasa"
print(aku)