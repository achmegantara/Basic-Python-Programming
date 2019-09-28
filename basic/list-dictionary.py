# tujuan dictionary adalah untuk membuat list dengan kata kunci
#sehingga tidak perlu memanggil list dengan menggunakan nomor indeks

#bentuk umum
aku = {
    "nama" : "achmad akbar",
    "url" : "github.com/achmegantara"
}
print(aku)

#dictionary dapat berisi apapun
pak_tani = {
    "nama" : "achmad akbar",
    "umur" : 22,
    "hobi" : ["coding","membaca","menulis"],
    "menikah" : False,
    "sosmed" : {
        "instagram" : "achmegantara",
        "github" : "achmegantara"
    }
}
#print(pak_tani)

#membuat dictionary dengan perintah dict()
warna_buah = dict(jeruk="orange", apel="merah", pisang="kuning")
print(warna_buah)

#mencetak nilai tertentu
print("nama saya adalah %s"%pak_tani["nama"])
print("Instagram : %s"%pak_tani["sosmed"]["instagram"])
print(pak_tani.get("menikah"))

#memanggil dengan perulangan
for key in pak_tani:
    print(pak_tani[key])

#mengganti nilai dari dalam dictionary
pak_tani["nama"] = "achmad megantara"
    
for key, val in pak_tani.items():
    print("%s : %s"%(key,val))
    
#menambahkan item ke dictionary
pak_tani.update({"password" : "12345"})

for key in pak_tani:
    print(pak_tani[key])

#mengambil panjang dictionary
print("total isi : %d"%len(pak_tani))
