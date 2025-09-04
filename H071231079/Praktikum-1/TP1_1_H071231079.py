#Menghitung Luas dan Keliling Segitiga
print("Menghitung Luas Permukaan dan Keliling Segitiga")
t = float(input('Masukkan nilai X = '))
a = float(input('Masukkan nilai Y = '))

#Menghitung Nilai Z(hipotenusa)
m = (a**2 + t**2)**0.5

luas = 0.5*a*t
keliling = t+a+m

print(f"Luas segitiga = {luas:.2f}")
print(f"Keliling segitiga = {keliling:.2f}")