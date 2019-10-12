#pada break, looping akan langsung berhenti
for i in range(1,10):
    print(i)
    if i is 5:
        print("angka telah ditemukan")
        break
else:
    print("Angka tidak ditemukan")
    
print("ini di luar looping")

#pada continue, looping akan dilanjutkan pada looping berikutnya
for i in range (1,10):
    if i is 6:
        print("ini adalah angka",i)
        continue
    print("nilai saat ini adalah",i)
else:
    print("akhir dari loop")
    
print("ini di luar loop")