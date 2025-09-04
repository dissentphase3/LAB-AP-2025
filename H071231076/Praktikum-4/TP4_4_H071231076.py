def catAndMouse(CatA, CatB, MouseC):
    jarak_A = abs(CatA - MouseC) #Menghitung jarak cat a dengan tikus
    jarak_B = abs(CatB - MouseC) #Menghitung jarak cat b dengan tikus

    if jarak_A < jarak_B : #Jika jarak A ke tikus < jarak B ke tikus = Cat A lebih dekat dengan tikus
        print ("Cat A")
    elif jarak_A > jarak_B : #Jika jarak A ke tikus > jarak B ke tikus = Cat B lebih dekat dengan tikus
        print ("Cat B")
    else : #Jarak antara cat A dan Cat B sama, maka tikus akan lolos
        print ("Mouse C")

CatA = int(input("CatA = "))
CatB = int(input("CatB = "))
MouseC = int(input("MouseC = "))

print(f"Cat and Mouse(Cat A = {CatA}, Cat B = {CatB}, Mouse C = {MouseC})")
catAndMouse(CatA, CatB, MouseC)