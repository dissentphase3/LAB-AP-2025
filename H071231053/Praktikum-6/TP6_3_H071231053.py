x = list(map(int,input("Masukkan beberapa angka: ").split()))

genap =set([ i for i in x if i%2 == 0])
ganjil =set([ i for i in x if i%2 !=0])
lima =set([ i for i in x if i%5 == 0])

print("Genap :",sorted(list(genap),reverse=True))
print("Ganjil :",sorted(list(ganjil),reverse=True))
print("Angka yang habis di bagi 5: ",sorted(list(lima),reverse=True))