angka = input("Masukkan beberapa angka: ").split()
angka = [int(i) for i in angka]

angka_genap = []
angka_ganjil = []
angka_dibagi5 = []

for i in angka :
    if i % 2 == 0 :
        angka_genap.append(i)
    else :
        angka_ganjil.append(i)
    if i % 5 == 0 :
        angka_dibagi5.append(i)

list_angkagenap = set(angka_genap)
list_angkaganjil = set(angka_ganjil)
list_angka_dibagi5 = set(angka_dibagi5)

print(f"Angka Genap: {sorted(list(list_angkagenap))}")
print(f"Angka Ganjil: {sorted(list(list_angkaganjil))}")
print(f"Angka yang habis dibagi 5: {sorted(list(list_angka_dibagi5))}")
