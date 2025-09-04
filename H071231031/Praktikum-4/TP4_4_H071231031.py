def catAndMouse(catA, catB, mosC):
    return "Cat A" if (catA - mosC) ** 2 < (catB - mosC) ** 2 else "Cat B" if (catB - mosC) ** 2 < (catA - mosC) ** 2 else "Mouse C"

catA = int(input("Masukkan posisi Cat A: "))
catB = int(input("Masukkan posisi Cat B: "))
mosC = int(input("Masukkan posisi Mouse C: "))

hasil = catAndMouse(catA, catB, mosC)
print(f"Hasil: {hasil}")