# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Pekan Pertama Praktikum Algoritma dan Pemrograman

print("\nSoal no. 3: Rumus Persamaan Kuadrat.\n")
    
a = float(input("Nilai a: "))
if a == 0:
    print("Nilai a harus bukan nol.")
    quit()
b = float(input("Nilai b: "))
c = float(input("Nilai c: "))

diskriminan = b**2 - 4*a*c

xa = (-b + (diskriminan)**0.5) / (2*a)
xb = (-b - (diskriminan)**0.5) / (2*a)

print(f"\nx1 = {xa:.2f}")
print(f"x2 = {xb:.2f}\n")