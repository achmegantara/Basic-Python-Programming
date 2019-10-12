#fungsi menggunakan argumen sederhana
def siswa(nama):
    print("Siswa ini bernama",nama)
    
siswa("achmad")

#fungsi menggunakan argumen keyword
def mahasiswa(nama,pelajaran):
    print("nama mahasiswa : ", nama)
    print("mata pelajaran : ",pelajaran)
    
mahasiswa(nama="achmad akbar", pelajaran="informatika")

#fungsi dengan default argumen
def user(nama="nama",id=0):
    print("nama user : ",nama)
    print("id user : ",id)

user(id=5,nama="megantara")
    

