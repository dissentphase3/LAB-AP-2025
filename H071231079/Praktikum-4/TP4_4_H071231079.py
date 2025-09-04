def catAndMouse(CatA, CatB, MouseC):
    a = abs(CatA - MouseC)
    b = abs(CatB - MouseC)
    if a < b:
        return "Cat A"
    elif a > b:
        return "Cat B"
    else:
        return "MouseC"
    
CatA = int(input("Masukkan posisi Cat A: "))
CatB = int(input("Masukkan posisi Cat B: "))
MouseC = int(input("Masukkan posisi Mouse C: "))

hasil = catAndMouse(CatA, CatB, MouseC)
print(hasil)