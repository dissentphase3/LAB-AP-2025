a = str(input("masukkan input pertama = "))
b = str(input("masukkan input kedua = "))
c = str(input("masukkan input ketiga = "))

if a == "vertebrado":
    if b == "ave":
        if c == "carnivoro":
            print("aguia")
        elif c == "onivoro":
            print("pomba")
        else:
            print("Invalid input")
    elif b == "mamifero":
        if c == "onivoro":
            print("homem")
        elif c == "herbivoro":
            print("vaca")
        else:
            print("Invalid input")
    else:
        print("Invalid input")

elif a == "invertebrado":
    if b == "inseto":
        if c == "hematofago":
            print("pulga")
        elif c == "herbivoro":
            print("lagarta")
        else:
            print("Invalid input")
    elif b == "anelideo":
        if c == "hematofago":
            print("sanguessuga")
        elif c == "onivoro":
            print("minhoca")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")
