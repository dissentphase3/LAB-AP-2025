# Input nilai a, b, dan c dari pengguna
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

# Menghitung argume1n
x1 = (-b + (b**2 - 4*a*c)** 0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)** 0.5)/ (2*a)

# Menampilkan hasil dengan maksimal dua angka di belakang koma
print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")
