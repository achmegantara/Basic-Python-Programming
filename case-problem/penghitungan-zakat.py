print("Penghitung jumlah zakat")
print("-----------------------")

def menu():
    print("Pilih penghitungan zakat")
    print("1. Zakat penghasilan")
    print("2. Zakat pergadangan")
    print("3. Zakat emas")
    print("4. Zakat tabungan")

def zakat_penghasilan():
    gaji_bulanan = int(input("Masukkan gaji bulanan : "))
    
    #menghitung nisab
    print("Pilihan nishab")
    print("1. Beras")
    print("2. Gabah")
    pilihan = int(input("Pilihan : "))
    if pilihan == 1:
        harga_beras = int(input("Masukkan harga beras per kg : "))
        nisab = 520*harga_beras
    elif pilihan == 2:
        harga_gabah = int(input("Masukkan harga gabah per kg : "))
        nisab = 653*harga_gabah
    
    if gaji_bulanan >= nisab:
        zakat = 0.025*gaji_bulanan
        print("Anda wajib membayar zakat")
        print("Zakat yang wajib anda bayarkan sebesar {0}".format(zakat))
    elif gaji_bulanan < nisab:
        print("Anda tidak wajib membayar zakat")    
def zakat_perdagangan():
    modal = int(input("Masukkan modal selama 1 tahun / nilai barang yang belum terjual : "))
    untung = int(input("Masukkan keuntungan selama 1 tahun : "))
    piutang = int(input("Masukkan piutang dagang : "))
    hutang_tempo = int(input("Masukkan hutang jatuh tempo : "))
    kerugian = int(input("Masukkan kerugian selama 1 tahun : "))
    harga_emas = int(input("Masukkan harga emas per gram saat ini : "))
    
    nisab = harga_emas*85
    total = modal+untung+piutang-hutang_tempo-kerugian
    
    if total >= nisab:
        zakat = total*0.025
        print("Zakat yang wajib dibayar sebesar {0}".format(zakat))
    elif total < nisab:
        print("Anda tidak wajib membayar zakat")    
def zakat_emas():
    emas_kepemilikan = int(input("Masukkan gram emas yang dimiliki : "))
    harga_emas = int(input("Masukkan harga emas : "))
    
    emas_to_rupiah = emas_kepemilikan*harga_emas
    
    if emas_kepemilikan >=85:
        zakat = emas_to_rupiah*0.025
        print("Zakat yang wajib dibayar sebesar {0}".format(zakat))
    elif emas_kepemilikan < 85:
        print("Anda tidak wajib membayar zakat")
def zakat_tabungan():
    tabungan = int(input("Masukkan jumlah tabungan : "))
    investasi = int(input("Masukkan nilai investasi yang dipunya : "))
    harga_emas = int(input("Masukkan harga emas per gram saat ini : "))
    
    total = tabungan+investasi
    nisab = 85*harga_emas
    
    if total >= nisab:
        zakat = total*0.025
        print("Zakat yang wajib dibayar sebesar {0}".format(zakat))
    elif total < nisab:
        print("anda tidak wajib membayar zakat")
    
menu()
while True:
    pilih = int(input("Masukkan pilihan : "))
    if pilih >0 and pilih <=4:
        break

if pilih == 1:
    zakat_penghasilan()
elif pilih == 2:
    zakat_perdagangan()
elif pilih == 3:
    zakat_emas()
elif pilih == 4:
    zakat_tabungan()
