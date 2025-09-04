data = list(map(int, input('Masukkan beberapa angka : ').split()))

genap = set([i for i in data if i % 2 == 0])
ganjil = set([i for i in data if i % 2 != 0])
bagi5 = set([i for i in data if i % 5 == 0])

print(f"Angka Genap : {sorted(list(genap))}") 
print(f"Angka Ganjil : {sorted(list(ganjil))}")
print(f"Angka habis dibagi 5 : {sorted(list(bagi5))}")
