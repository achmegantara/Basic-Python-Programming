def fungsi_nilai_total(harian,uts,uas):
    nilai_harian = float(harian)*0.3
    nilai_uts = float(uts)*0.3
    nilai_uas = float(uas)*0.4
    
    total = nilai_harian+nilai_uts+nilai_uas
    return total

def factor_index(nilai):
    if nilai >=0 and nilai <20:
        var_indeks = "E"
    elif nilai >=20 and nilai <40:
        var_indeks = "D"
    elif nilai >=40 and nilai <60:
        var_indeks = "C"
    elif nilai >=60 and nilai <80:
        var_indeks = "B"
    elif nilai >=80 and nilai <100:
        var_indeks = "A"

    return var_indeks

print("Program menghitung nilai akhir")
print("------------------------------")

harian = int(input("Masukkan nilai harian : "))
uts = int(input("Masukkan nilai uts : "))
uas = int(input("Masukkan nilai uas : "))

indeks = fungsi_nilai_total(harian,uts,uas)
print("Nilai anda adalah : {0}".format(factor_index(indeks)))
