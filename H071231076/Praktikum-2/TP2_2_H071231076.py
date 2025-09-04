Input_pertama = str(input("Masukkan input pertama :"))
Input_kedua = str(input("Masukkan input kedua :"))
Input_ketiga = str(input("Masukkan input ketiga :"))
match (Input_pertama, Input_kedua, Input_ketiga) :
    case "vertebrado", "ave", "carnivoro":
            print("agula")
    case "vertebrado", "ave", "onivoro":
            print("pomba")
    case "vertebrado", "mamifero", "onivoro" :
            print("homem")
    case "vertebrado", "mamifero", "herbivoro" :
            print("vaca")
    case "invertebrado", "inseto", "hematofago":
            print("pulga")
    case "invertebrado", "inseto", "herbivoro" :
            print("lagarta")
    case "invertebrado", "anelideo", "hematofago":
            print("sangeussuga")
    case "invertebrado", "anelideo", "onivoro" :
            print ("minhoca")
    case _:
         print("Invalid input")