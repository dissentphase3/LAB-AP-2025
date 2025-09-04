def maksimum(*Arg):
    angka_terbesar = 0
    for num in Arg:
        for i in num:
            if i > angka_terbesar:
                angka_terbesar = i
    return angka_terbesar
Angka = []
while True:
    Masukan = (input("Masukan input "))
    if Masukan.lower() == 'selesai':
        break
    Angka.append(int(Masukan))
print(maksimum(Angka))
