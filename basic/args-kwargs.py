#tanda bintang(*) disebut args, digunakan untuk membuat fungsi dengan parameter 
#yang masih tidak jelas jumlahnya
# bintang satu (*) akan membuat parameter fungsi menjadi tupple
#sedangkan untuk bintang dua(**) akan membuat parameter menjadi dictionary
def panggil(*nama):
    print("daftar nama orang yang dipanggil")
    for orang in nama:
        print(orang)
        
panggil("achmad","akbar","megantara")