#Tuple adalah struktur data yang digunakan untuk menyimpan sekumpulan data. Tupe bersifat immutablem artinya isi tuple tidak bisa diubah dan dihapus. namun, dapat kita isi dengan berbagai macam nilai dan objek

#inisialisai dan memberi nilai pada tupple
t = (1234, 4321, "hello", 0.56)

#membuat tuple kosong
kosong = ()

#untuk membuat tuple dengan isi satu nilai harus diberi koma
satu = ("isinya",)

#mengakses nilai pada tuple
print(t[1])

#memotong tupple
print(t[1:3])

#mengambil panjang tupple
print("jumlah isi : %d"%len(t))

#tuple nested
tuple1 = "aku", "kamu", "dia"
tuple2 = ("selama",3,"tahun")
tuple3 = (tuple1,tuple2)

print(tuple3)

tuple4 = ([1,2,3], {'nama', 'Petanikode',"rank", 123}, True)

print(tuple4)

#sequence unpacking
#membuat tuple
web = 123, "petani kode", "http.github.com"

#lalu di-unpacking
id_web, nama, url = web

#mari dicetak
print(id_web)
print(nama)
print(url)