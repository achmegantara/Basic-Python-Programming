#cara mengambil input
#pada python2
#input() = angka
#raw_input() = teks

#pada python3
#input() = angka dan teks

nama = input("Sebuah Teks : ")
umur = input("Masukkan umur : ")

#mencetak input
print("Nama saya",nama,"umur ",umur)
print(nama,umur)

#fungsi format()
#untuk menggabungkan teks dengan isi variabel

nama2 = input("Nama user : ")
print("Hallo {} apa kabar?".format(nama2))