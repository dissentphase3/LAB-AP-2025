# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Pekan Pertama Praktikum Algoritma dan Pemrograman

print("\nSoal no. 2: Konversi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit.\n")

suhu = float(input("Masukkan suhu dalam Celcius: "))
kelvin = int(suhu + 273)
reamur = int(4/5 * suhu)
fahrenheit = int((suhu * 9/5) + 32)

print(f"\nHasil konversi dari suhu {int(suhu)}°C ke Kelvin adalah {kelvin} K")
print(f"Hasil konversi dari suhu {int(suhu)}°C ke Reamur adalah {reamur}°R")
print(f"Hasil konversi dari suhu {int(suhu)}°C ke Fahrenheit adalah {fahrenheit}°F\n")