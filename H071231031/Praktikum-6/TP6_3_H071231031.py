x = input("Masukkan angka-angka ")

L1 = [int(num) for num in x.split(' ')]


Genap, Ganjil, dibagi = [], [], []

for num in L1:
    if num % 2 == 0:
        Genap.append(num)
    else:
        Ganjil.append(num)
    
    if num % 5 == 0:
        dibagi.append(num)
        
x = list(set(Genap))
x.sort()
y = list(set(Ganjil))
y.sort()
z = list(set(dibagi))
z.sort()

print("Angka Genap:", x)
print("Angka Ganjil:", y)
print("Angka yang habis dibagi 5:", z)
