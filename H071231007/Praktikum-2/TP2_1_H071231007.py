print(f"1.Laki-laki")
print(f"2.Perempuan")
g = int(input("Masukkan jenis kelamin anda: "))

if g != 1 and g != 2:
    print(f"Data anda tidak valid")
else:
    t = float(input("Masukkan tinggi badan anda (cm): ")) / 100
    b = float(input("Masukkan berat badan anda (kg): "))
    bmi = (b / t**2)

if g == 1:
    if 27 <= bmi:
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}")
    elif 24 <= bmi < 27:
        print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
    elif 18 <= bmi < 24:
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif bmi < 18:
        print(f'Anda tergolong Underweight dengan BMI {bmi:.2f} ')
elif g == 2:
    if 28 <= bmi:
        print(f'Anda tergolong Obese dengan BMI {bmi:.2f}')
    elif 24 <= bmi < 28:
        print(f'Anda tergolong Overweight dengan BMI {bmi:.2f}')
    elif 17 <= bmi < 24:
        print(f'Anda tergolong Normal dengan BMI {bmi:.2f}')
    elif bmi < 17:
        print(f'Anda tergolong Underweigt dengan BMI {bmi:.2f}')
else: 
    print('Data tidak valid ')

