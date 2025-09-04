def angka_terbesar(*daftar_angka):
    print(daftar_angka)
    angka_terbesar = daftar_angka[0]
    for angka in daftar_angka:
        if angka > angka_terbesar:
            angka_terbesar = angka
    return angka_terbesar

nums = []
print("\nUji")
while True:
    
    
    y = input("Masukkan input : ")
    if y.lower() == "selesai":
        break
    angka = int(y)
    nums.append(angka)

print(angka_terbesar(*nums))
