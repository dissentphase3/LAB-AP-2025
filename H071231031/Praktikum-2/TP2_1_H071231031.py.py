print("Pilih Gender Anda")
print("1. Pria")
print("2. Wanita")
gender = input("= ")

if gender == "1":
    bb_batas = [18, 24, 27]
elif gender == "2":
    bb_batas = [17, 24, 28]
else:
    print("Pilihan tidak valid")
    exit()

tb_cm = float(input("Masukkan tinggi badan (cm): "))
bb_kg = float(input("Masukkan berat badan (kg): "))

tb_meter = tb_cm / 100
bmi = bb_kg / (tb_meter ** 2)

if bmi < bb_batas[0]:
    kategori = "Underweight"
elif bmi < bb_batas[1]:
    kategori = "Normal"
elif bmi < bb_batas[2]:
    kategori = "Overweight"
else:
    kategori = "Obese"

print(f"Anda tergolong {kategori} dengan BMI {bmi:.2f}")
