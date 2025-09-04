gender = int(input("Pilih Gender Anda \n1.Pria \n2.Wanita \n= "))
if gender != 1 and gender != 2:
    print ("Mohon pilih 1 atau 2")
    exit()
else:
    tinggiBadan = float(input("Masukkan tinggi badan (cm) : "))
    beratBadan = float(input("Masukkan berat badan (kg) : "))

    BMI = beratBadan/(tinggiBadan/100)**2

    if gender == 1:
        if BMI < 18:
            kategori = "Underweight"
        elif BMI >=18 and BMI <= 23.9:
            kategori = "Normal"
        elif BMI >=24 and BMI <= 26.9:
            kategori = "Overweight"
        elif BMI >=27:
            kategori = "Obese"
    elif gender == 2:
        if BMI < 17:
            kategori = "Underweight"
        elif BMI >=17 and BMI <= 23.9:
            kategori = "Normal"
        elif BMI >=24 and BMI <= 27.9:
            kategori = "Overweight"
        elif BMI >=28:
             kategori = "Obese"
print(f"Anda tergolong {kategori} dengan BMI {BMI:.2f}")