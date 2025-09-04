ganjil, genap, bagi5 = set(), set(), set()

masuk = input("Masukkan beberapa angka: ").split()
for x in masuk:
    ubah = int(x)
    if ubah % 2 != 0:
        ganjil.add(ubah)
    elif ubah % 2 == 0:
        genap.add(ubah)
    if ubah % 5 == 0: 
        bagi5.add(ubah)

print("Angka Genap:", sorted(list(genap),reverse=True))
print("Angka Ganjil:", sorted(list(ganjil),reverse=True))
print("Angka yang habis dibagi 5:", sorted(list(bagi5),reverse=True))


