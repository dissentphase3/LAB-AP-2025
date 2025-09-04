#Mengkonversi suhu satuan Celsius ke Kelvin, Reamur, dan Fahrenheit

print("Konversi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
suhu = float(input("Masukkan Suhu dalam Celsius = "))

print(f"Hasil konversi dari suhu {(int(suhu))} derajat celcius ke Kelvin adalah : {(int(suhu + 273))}K")
print(f"Hasil konversi dari suhu {(int(suhu))} derajat celcius ke Reamur adalah : {(int(suhu*4//5))}R")
print(f"Hasil konversi dari suhu {(int(suhu))} derajat celcius ke Fahrenheit adalah : {(int(suhu*9//5) + 32)}F")