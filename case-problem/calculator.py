#proses operasi dan tampilkan hasil
def penjumlahan(x,y):
    hasil = x + y
    print("Hasil penjumlahan = {0}".format(hasil))

def pengurangan(x,y):
    hasil = x-y
    print("Hasil pengurangan = {0}".format(hasil))

def pembagian(x,y):
    hasil = x/y
    print("Hasil pembagian = {0}".format(hasil))

def perkalian(x,y):
    hasil = x*y
    print("Hasil perkalian = {0}".format(hasil))


#input bilangan
bil1 = float(input("Masukkan bilangan pertama : "))
bil2 = float(input("Masukkan bilangan kedua : "))

#pilih operasi 
print("Pilih operasi matematik")
print("1.Penjumlahan\n2.Pengurangan\n3.Pembagian\n4.perkalian")

#input pilihan operasi
while True:
    pil = int(input("Pilihan operasi [1-4] : "))
    if(pil>0 and pil<5):
        break

if pil is 1:
    penjumlahan(bil1,bil2)
elif pil is 2:
    pengurangan(bil1,bil2)
elif pil is 3:
    pembagian(bil1,bil2)
elif pil is 4:
    perkalian(bil1,bil2)