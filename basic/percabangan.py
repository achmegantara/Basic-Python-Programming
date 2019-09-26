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