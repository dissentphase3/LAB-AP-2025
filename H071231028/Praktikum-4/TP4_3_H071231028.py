
def angka_terbesar(*daftar_angka):
    angka_terbesar = daftar_angka[0]
    for angka in daftar_angka:
        if angka > angka_terbesar:
            angka_terbesar = angka
    return angka_terbesar

daftar_angka = []

while True:
    inputan = input("Masukkan Angka : ")
    if inputan == "selesai":
        break
    try:
        angka = int(inputan)
        daftar_angka.append(angka)
    except ValueError:
        print("Input tidak valid")

if daftar_angka:
    print("angka terbesarnya adalah:", angka_terbesar(daftar_angka))
else:
    print("Daftar kosong")



















