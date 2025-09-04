# Input suhu dalam Celcius 
suhu_celcius = float(input("Masukkan Suhu dalam Celcius: "))

# Konversi ke Kelvin
suhu_kelvin = suhu_celcius + 273

# Konversi ke Reamur
suhu_reamur = suhu_celcius * 0.8

# Konversi ke Fahrenheit
suhu_fahrenheit = (suhu_celcius * 9/5) + 32

# Hasil
print(f"Hasil konversi dari suhu {int(suhu_celcius)} derajat Celcius ke Kelvin adalah: {int(suhu_kelvin)}K")
print(f"Hasil konversi dari suhu {int(suhu_celcius)} derajat Celcius ke Reamur adalah {int(suhu_reamur)}R")
print(f"Hasil konversi dari suhu {int(suhu_celcius)} derajat Celcius ke Fahrenheit adalah: {int(suhu_fahrenheit)}F")
