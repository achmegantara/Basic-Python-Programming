#struktur dasar
lulus = input("apakah kamu lulus? [ya/tidak]: ")
if lulus == "tidak":
    print("Kamu harus ikut ujian")
    
#contoh case
total_belanja = int(input("Total Belanja : Rp"))

bayar = total_belanja

if total_belanja > 100000:
    print("Kamu mendapatkan bonus minuman dingin")
    print("dan diskon 5%")
    
    diskon = total_belanja*5/10
    bayar = total_belanja - diskon
    
#cetak struk
print("total yang harus dibayar : Rp %s " % bayar)
print("Terima kasih telah berbelanja")

#contoh case 2
umur = int(input("Berapa umur kamu : "))

if umur >= 18:
    print("Kamu boleh membuat sim")
else:
    print("Kamu tidak boleh membuat sim")
