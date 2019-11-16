def menu():
    print("Pilih bentuk bidang")
    print("1. Persegi")
    print("2. Persegi panjang")
    print("3. Segitiga")
    print("4. Lingkaran")

def persegi():
    sisi = int(input("Masukkan panjang sisi : "))
    area = sisi*sisi
    print("Luas dari persegi tersebut = {0}".format(area))

def persegipanjang():
    panjang = int(input("Masukkan nilai panjang = "))
    lebar = int(input("Masukkan nilai lebar = "))
    area = panjang*lebar
    print("Luas persegi panjang tersebut adalah = {0}".format(area))
    
def segitiga():
    alas = int(input("Masukkan nilai alas : "))
    tinggi = int(input("Masukkan nilai tinggi : "))
    area = (alas*tinggi)/2
    print("Luas dari segitiga tersebut adalah = {0}".format(area))
    
def lingkaran():
    phi = 3.14
    radius = int(input("Masukkan nilai radius : "))
    area = (float(phi)*float(radius**2))
    print("Luas dari lingkaran tersebut adalah = {0}".format(area))
    
menu()
pilihan = int(input("Masukkan pilihan : "))
if pilihan == 1:
    persegi()
elif pilihan == 2:
    persegipanjang()
elif pilihan == 3:
    segitiga()
elif pilihan == 4:
    lingkaran()
    
