# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Praktikum Pekan Kedua
print("\nMenghitung BMI\n==============")
gender = input("\nPilih jenis kelamin Anda:\n1. Pria\n2. Wanita\n")
if gender.isdigit() == False:
    print("\nInvalid input.\n")
    quit()
gender = int(gender)
if gender < 1 or gender > 2:
    print("\nJumlah jenis kelamin hanyalah 2 (dua).\nJika kurang atau lebih dari itu, saya sarankan Anda ke RSJ.\n")
    quit()
    
tinggi = float(input("\nMasukkan tinggi badan Anda (cm): ")) / 100
if tinggi <= 0:
    print("\nInvalid input.\n")
    quit()

berat = float(input("Masukkan berat badan Anda (kg): "))
if berat <= 0:
    print("\nInvalid input.\n")
    quit()

bmi = berat/(tinggi**2)

match gender:
    case 1:
        if bmi < 18:
            ket = "Underweight"
        elif 18 <= bmi < 24:
            ket = "Normal"
        elif 24 <= bmi < 27:
            ket = "Overweight"
        else:
            ket = "Obese"

    case 2:
        if bmi < 17:
            ket = "Underweight"
        elif 17 <= bmi < 24:
            ket = "Normal"
        elif 24 <= bmi < 28:
            ket = "Overweight"
        else:
            ket = "Obese"

    case _:
        print("\nInvalid input.\n")

print(f"\nAnda tergolong {ket} dengan BMI {bmi:.2f}")