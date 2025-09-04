# mengkonfert suhu celsius ke kelvin,reamur, dan fahrenheit
suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))

suhu_kelvin = int(suhu_celcius + 273.15)
suhu_reamur = int(4/5 * suhu_celcius)
suhu_fahrenheit = int((suhu_celcius * 9/5) + 32)

# Menampilkan hasil konversi dalam format string
print(f"Hasil konversi dari suhu {suhu_celcius} C jika dikonvert ke Fahrenheit: {suhu_fahrenheit}F")
print(f"Hasil konversi dari suhu {suhu_celcius} C jika dikonvert ke Kelvin: {suhu_kelvin}K")
print(f"Hasil konversi dari suhu {suhu_celcius} C jika dikonvert ke Reamur: {suhu_reamur}R")
