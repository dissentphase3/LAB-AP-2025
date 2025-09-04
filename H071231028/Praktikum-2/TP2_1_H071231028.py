
print("Pilih Gender Anda")
print("1. Pria")
print("2. Wanita")
gender = int(input("= "))


tinggi_badan = float(input("Masukkan tinggi badan (cm) : "))
berat_badan = float(input("Masukkan berat badan (kg) : "))


tinggi_badan_meter = tinggi_badan / 100
bmi = berat_badan / (tinggi_badan_meter ** 2)

kategori = None 

if gender == 1:
    if bmi < 18:
        kategori = "Underweight"
    elif 18 <= bmi < 24:
        kategori = "Normal"
    elif 24 <= bmi < 27:
        kategori = "Overweight"
    else:
        kategori = "Obese"
elif gender == 2:  
    if bmi < 17:
        kategori = "Underweight"
    elif 17 <= bmi < 24:
        kategori = "Normal"
    elif 24 <= bmi < 28:
        kategori = "Overweight"
    else: 
        kategori = "Obese"


if kategori is not None :
    print(f"Anda tergolong {kategori} dengan BMI {bmi:.2f}")
else:
    print("invalid input")

