# Muhammad Qaffal Al Fifaiz | H071231032 | Tugas Praktikum Pekan Kedua

print(f"\n{'='*33}\nPenghitung Jumlah Tagihan Listrik\n{'='*33}\n")

# Input golongan dan penanganan traceback-nya
gol = input("Pilih golongan:\n1. R1\t4. B2\t7. P1\n2. R2\t5. B3\n3. R3\t6. I3\n").upper()
# if gol not in ['R1','R2','R3','B2','B3','I3','P1']:
#     print("\nInvalid data.\n")
#     quit()

# Input daya dan penanganan traceback-nya
daya = input("\nDaya: ")
if daya.isdigit() == False:
    print("\nInvalid data.\n")
    quit()
daya = int(daya)

# Penentuan tarif per kWh
match gol:
    case 'R1':
        if daya == 900:
            TARIF = 1352
        elif daya == 1300 or daya == 2200:
            TARIF = 1444.70
        else:
            print("\nInvalid data.\n")
            quit()
                
    case 'R2':  
        if 3500 <= daya <= 5500:
            TARIF = 1699.53
        else:
            print("\nInvalid data.\n")
            quit()

    case 'R3':     
        if daya >= 6600:
            TARIF = 1699.53
        else:
            print("\nInvalid data.\n")
            quit()

    case 'B2': 
        if 6600 <= daya <= 200000:
            TARIF = 1444.70
        else:
            print("\nInvalid data.\n")
            quit()

    case 'B3':        
        if daya > 200000:
            TARIF = 1114.74
        else:
            print("\nInvalid data.\n")
            quit()

    case 'I3':      
        if daya >= 200000:
            TARIF = 1314.12
        else:
            print("\nInvalid data.\n")
            quit()

    case 'P1':        
        if 6600 <= daya <= 200000:
            TARIF = 1523.28
        else:
            print("\nInvalid data.\n")
            quit()

    case _:
        print("Invalid input.")
        quit()

# Input pemakaian dan penanganan traceback-nya
pakai = input("Pemakaian: ")
if pakai.isdigit() == False:
    print("\nInvalid data.\n")
    quit()
pakai = int(pakai)

# Menghitung jumlah tagihan sesuai dengan data yang telah dimasukkan
tagihan = float(TARIF * pakai)

# Mengatur format tulisan jumlah tagihan sesuai dengan Kaidah Bahasa Indonesia dan mencetak jumlah tagihan
depan,koma = str(tagihan).split('.')
depan = int(depan); koma = koma[:2]
depan = f"{depan:,}".replace(',','.')
print(f'\nJumlah tagihan Anda sebesar: Rp. {depan},{koma}\n')