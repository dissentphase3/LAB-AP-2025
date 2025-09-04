# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Praktikum Pekan Kedua

print("\nPencocokan Organisme\n====================")
a = input("\nMasukkan inputan pertama: ").lower()
b = input("Masukkan inputan kedua: ").lower()
c = input("Masukkan inputan ketiga: ").lower()
match a,b,c:
    case 'vertebrado','ave','carnivoro':
        print('\nagula\n')
    case 'vertebrado','ave','onivoro':
        print('\npomba\n')
    case 'vertebrado','mamifero','onivoro':
        print('\nhomem\n')
    case 'vertebrado','mamifero','herbivoro':
        print('\nvaca\n')
    case 'invertebrado','inseto','hematofago':
        print('\npulga\n')
    case 'invertebrado','inseto','herbivoro':
        print('\nlagarta\n')
    case 'invertebrado','anelideo','hematofago':
        print('\nsanguessuga\n')
    case 'invertebrado','onivoro','hematofago':
        print('\nminhoca\n')
    case _:
        print('\nInvalid input.\n')