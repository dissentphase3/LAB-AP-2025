
def catAndMouse():
    try:
        catA = int(input("Masukkan jarak tom A ke jerry C: "))
        catB = int(input("Masukkan jarak tom B ke jerry C: "))
        mosC = int(input("Masukkan jarak jerry C: "))
        
        distanceA = abs(catA - mosC)
        distanceB = abs(catB - mosC)
        
        if distanceA < distanceB:
            print("Cat A")
        elif distanceB < distanceA:
            print("Cat B")
        else:
            print("Mouse C")
    except ValueError:
        print("Masukkan jarak .")

catAndMouse()
