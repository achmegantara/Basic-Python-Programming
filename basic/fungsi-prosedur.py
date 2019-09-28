# #struktur umum fungsi
# def hello():
#     print("Hello")
#     print("world")

# hello()

# #fungsi dengan parameter
# def salam(ucapan):
#     print(ucapan)

# salam("Selamat Siang")

# #fungsi dengan multi parameter
# def luas_segitiga(alas,tinggi):
#     luas = (alas*tinggi)/2
#     print("Luas segitiga : %d"%luas)

# luas_segitiga(6,7)

# #fungsi yang mengembalikan nilai
# def luas_persegi(sisi):
#     luas = sisi*sisi
#     return luas

# print("Luas persegi : %d"%luas_persegi(6))

# #variabel global dan lokal 

# #ini variabel global
# nama = "Achmad megantara"
# versi = "1.0.1"

# def help():
#     nama = "programku"
#     versi = "1.0.2"
#     #mengakses variabel lokal
#     print("Nama : %s"%nama)
#     print("Versi : %s"%versi)
    
# #mengakses variabel global
# print("Nama : %s"%nama)
# print("versi : %s"%versi)

# help()

#urutan pemanggilan variabel
#lokal -> global -> buildin
    
#contoh program dengan fungsi
buku = []

#fungsi untuk menampilkan semua data
def show_data():
    if(len(buku)) <= 0:
        print("Belum ada data")
    else :
        for indeks in range(len(buku)):
            print("[%d] %s "%(indeks,buku[indeks]))
            
def insert_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)

def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku : "))
    if(indeks > len(buku)):
        print("ID Salah")
    else :
        judul_baru = input("Judul baru : ")
        buku[indeks] = judul_baru

def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku : "))
    if(indeks > len(buku)):
        print("ID salah")
    else :
        buku.remove(buku[indeks])

def show_menu():
    print("\n")
    print("-------------MENU-------------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = int(input("Pilih Menu > "))
    print("\n")
    
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else :
        print("Salah pilih")
    
if __name__ == "__main__":
    while(True):
        show_menu()