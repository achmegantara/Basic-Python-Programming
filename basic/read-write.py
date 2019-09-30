#struktur umum membaca file di python
#file = open("file.txt", "r")
# file => nama objek untuk menampung file
# file.txt => nama file (path)
# "r" => mode read
# "w" => untuk menulis file (replace)
# "a" => append/menambah file 
# "r+" => membaca sekaligus menulis data ke file

#contoh membuka file
path = 'file-io/tulisan.txt'
file_tulisan = open(path,'r')
# tulisan = file_tulisan.readlines()
isi = file_tulisan.read()

#baca isi file
# print(tulisan)
# print(tulisan[1])

# for teks in tulisan:
#     print(teks)

print(isi)

#tutup file
file_tulisan.close()

print("Selamat datang di Program Biodata")
print("---------------------------------")

#mengambil input dari user
nama = input("Nama : ")
umur = int(input("Umur : "))
alamat = input("alamat : ")

teks = "Nama : {}\n, Umur : {}\n, alamat : {}\n".format(nama,umur,alamat)

file_bio = open("file-io/biodata.txt", "a")

file_bio.write(teks)

file_bio.close()