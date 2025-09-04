nt1=input("Masukkan Input Pertama : ")
nt2=input("Masukkan Input Kedua : ")
nt3=input("Masukkan Input Ketiga : ")


match (nt1, nt2, nt3):
    case ("vertebrado", "ave", "carnivoro"):
        print("aguia")
    case ("vertebrado", "ave", "onivoro"):
        print("pomba")
    case ("vertebrado", "mamifero", "onivoro"):
        print("homem")
    case ("vertebrado", "mamifero", "herbivoro"):
        print("vaca")
    case ("invertebrado", "inseto", "hematofago"):
        print("pulga")
    case ("invertebrado", "inseto", "herbivoro"):
        print("lagarta")
    case ("invertebrado", "anelideo", "hematofago"):
        print("sanguessuga")
    case ("invertebrado", "anelideo", "onivoro"):
        print("minhoca")
    case _:

        print("Invalid input")