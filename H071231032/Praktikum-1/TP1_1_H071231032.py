# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Pekan Pertama Praktikum Algoritma dan Pemrograman

print("\nSoal no. 1: Mencari Luas dan Keliling Segitiga XYZ.\n")

tinggi = float(input("Panjang sisi X (tinggi segitiga) dalam cm: "))
alas = float(input("Panjang sisi Y (alas segitiga) dalam cm: "))
miring = ((tinggi ** 2) + (alas ** 2)) ** 0.5

luas = 0.5 * alas * tinggi
keliling = tinggi + alas + miring

print(f"\nLuas segitiga: {luas:.2f} cm^2\nKeliling segitiga: {keliling:.2f} cm")