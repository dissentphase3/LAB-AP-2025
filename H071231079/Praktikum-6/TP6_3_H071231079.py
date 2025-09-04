listAngka = set([int(angka) for angka in input("Masukkan beberapa angka : ").split()])

ganjil = []
genap = []
habisLima = []

for angka in listAngka:
    if angka % 2 == 0:
        genap.append(angka)
    else:
        ganjil.append(angka)
    if angka % 5 == 0:
        habisLima.append(angka)

print(f"Angka genap : {genap}\nAngka ganjil : {ganjil}\nAngka yang habis dibagi 5 : {habisLima}")