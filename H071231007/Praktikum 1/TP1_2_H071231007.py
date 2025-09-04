print('Konversi suhu dari celcius ke kelvin, Reamur dan Fahrenheit')

p = float(input('Masukkan suhu dalam Celcius : '))

kelvin = int(p+273)
reamur = int(4/5*p)
fahrenheit = int((9/5*p)+32)

print(f'Hasil konversi dari suhu {int(p)} derajat celcius ke kelvin adalah       :{kelvin}K')
print(f'Hasil konversi dari suhu {int(p)} derajat celcius ke reamur adalah       :{reamur}R')
print(f'Hasil konversi dari suhu {int(p)} derajat celcius ke fahrenheit adalah   :{fahrenheit}F')

print("Celcius Ke Reamur = ", reamur,"R")

