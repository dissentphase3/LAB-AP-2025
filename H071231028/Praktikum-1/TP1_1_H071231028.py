# Input sisi x dan y
x = float(input("Masukkan panjang sisi x: "))
y = float(input("Masukkan panjang sisi y: "))

# Menghitung panjang sisi z
z = (x**2 + y**2)**0.5

# Menghitung luas permukaan
keliling = 0.5 * x * y

# Menghitung keliling
luas  = x + y + z

print(f"panjang sisi z : {z:.2f}")
print(f"luas permukaan :{luas:.2f}")
print(f"keliling : {keliling:.2f}")



