#perulangan for
#struktur umum

#for indek in range (banyak_perulangan)
    #jalankan kode ini
    #kode ini juga
#kode ini tidak akan diulang

ulang = 10
for i in range(ulang):
    print("Perulangan ke-",i)
    
item = ['kopi','nasi','teh','jeruk']

for isi in item:
    print(isi)

jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulangi lagi tidak? ")
    if jawab == 'tidak':
        break

print("total perulangan : ",hitung)