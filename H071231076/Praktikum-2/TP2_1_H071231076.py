jenis_kelamin = input("Masukkan jenis kelamin anda\n1. Pria \n2. Wanita\n =") 
tinggi = float(input("Masukkan tinggi badan Anda (cm) :"))
berat = float(input("Masukkan berat badan Anda (kg) :"))

tinggi = tinggi/100

bmi = berat / (tinggi **2)

if jenis_kelamin == "1" :
    if bmi < 18 :
        print(f"Anda tergolong underweight {bmi:.2f}")
    elif 18 <= bmi < 23.9 :
        print(f"Anda tergolong normal {bmi:.2f}")
    elif 24 <= bmi < 26.9 :
        print(f"Anda tergolong overweight {bmi:.2f}")
    else :
        print(f"Anda tergolong obese {bmi:.2f}")
        
if jenis_kelamin == "2" :
    if bmi < 17 :
        print(f"Anda tergolong underweight {bmi:.2f}")
    elif 17 <= bmi < 23.9 :
        print(f"Anda tergolong normal {bmi:.2f}")
    elif 24<= bmi < 27.9 :
        print(f"Anda tergolong overweight {bmi:.2f}")
    else :
        print(f"Anda tergolong obese {bmi:.2f}")