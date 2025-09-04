print('Pilih Gender Anda')
print('1. Pria')
print('2. Wanita')
opsi = str(input('= '))

if opsi == '1': 
    gender = "pria"
elif opsi == '2' :
    gender = "wanita"
else: 
    print('invalid input')  
    exit()

tinggi_badan =  float(input("masukkan tinggi badan(cm): "))
berat_badan =   float(input("masukkan berat badan(kg): "))
bmi = berat_badan / (((tinggi_badan)/100)** 2)
kategori_bmi = None

if gender == "pria": 
    if bmi < 18 :  
        kategori_bmi = "underweight"
    elif 18 <= bmi < 24 :  
        kategori_bmi = "normal"
    elif 24 <= bmi < 26.9 : 
        kategori_bmi = "overweight"
    elif bmi >= 27 :
        kategori_bmi = "obesitas"

elif gender == "wanita":
    if bmi < 17 :  
        kategori_bmi = "underweight"
    elif 17 <= bmi < 24 : 
        kategori_bmi = "normal"
    elif 24 <= bmi < 27.9 :  
        kategori_bmi = "overweight"
    elif bmi >= 28 :  
        kategori_bmi = "obesitas"

if kategori_bmi:   
    print(f"Anda tergolong {kategori_bmi} dengan BMI {bmi:.2F} ")
else:
    print("coba tentuin lagi jenis kelaminnya")

