#Input variabel
x = float(input("Panjang sisi X: "))
y = float(input("Panjang sisi Y: "))

#Menghitung luas
luas = (x * y) / 2

#Menghitung panjang sisi Z menggunakan teorema Pythagoras
z = (x**2 + y**2)**0.5

#Menghitung keliling
keliling = x + y + z

#Cetak hasil
print(f"Luas Permukaan: {luas:.2f}")
print(f"Keliling: {keliling:.2f}")
