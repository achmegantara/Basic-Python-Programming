#cara membuat list
#list = array

#membuat list kosong
warna = []

#membuat list dengan isi
hobi = ['membaca']

#semua jenis data dapat dimasukkan
laci = ['buku',21,True,34.12]
buah = ['apel','jeruk','mangga','pisang']

#mencetak list
print(buah[2])

#contoh case 1
my_friends = ["Anggun", "dian", "agung", "Adi", "Adam"]

#menampilkan indeks tertentu
print("Isi indeks ke-3 adalah : ",my_friends[3])

#menampilkan semua isi dari list
print("Semua teman ada : {}".format(len(my_friends)))
for friend in my_friends:
    print(friend)
    
#mengganti nilai list
print(buah[2])
buah[2] = "kelapa"
print(buah[2])

#menambahkan item list
#prepend(item) = menambah item dari depan
#append(item) = menambahkan item dari belakang
#insert(index,item) = menambahkan item dari indeks tertentu
buah.append("manggis")
print(buah)

#contoh case 2
stop = False
i = 0

while(not stop):
    warna_baru = input("Inputkan warna yang ke-{} ".format(i))
    warna.append(warna_baru)
    
    #increment i
    i += 1
    
    tanya = input("Mau isi lagi? (y/t) : ")
    if(tanya == "t"):
        stop = True
        
print("="*10)
print("Kamu memiliki {} warna".format(len(warna)))
for wrn in warna:
    print("-",warna)
    
#delete isi dalam list
todo_list = [
    "Belajar python",
    "Belajar Django",
    "Belajar MongoDB",
    "Belajar sulap"
]

del todo_list[3]
print(todo_list)

#memotong list
print(todo_list[1:2])

#list multidimensi
list_minuman = [
    ["kopi","susu","Teh"],
    ["Jus apel","Jus melon","Jus jeruk"],
    ["Es campur","Es teler","Es tebu"]
]

print(list_minuman[2][0])