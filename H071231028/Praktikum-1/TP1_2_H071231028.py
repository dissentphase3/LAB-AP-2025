# Input suhu dalam Celsius
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Konversi suhu dari celcius ke kelvin, Reamur, dan Fahrenheit
kelvin = celsius + 273
reamur = celsius * 0.8
fahrenheit = (celsius * 9/5) + 32

# Hasil konversi
print(f"Hasil konversi dari suhu Celsius ke kelvin adalah= {int(kelvin)}K")
print(f"Hasil konversi dari suhu celsius ke reamur adalah = {int(reamur)}R ")
print(f"Hasil konversi dari suhu celsius ke fahrenheit adalah = {int(fahrenheit)}F ")

