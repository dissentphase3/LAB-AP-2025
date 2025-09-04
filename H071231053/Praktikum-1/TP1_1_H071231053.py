# Menghitung keliling dan luas segitiga

sisi_x = float(input("Masukkan panjang sisi X: ")) # sisi alas
sisi_y = float(input("Masukkan panjang sisi Y: ")) # sisi tinggi 
sisi_z = (sisi_x ** 2 + sisi_y ** 2) ** 0.5 # sisi miring 

keliling = sisi_x + sisi_y + sisi_z

luas = 1/2 * sisi_x * sisi_y

# Menampilkan hasil dalam format string
print(f"Panjang sisi Z: {sisi_z:.2f}")  
print(f"Luas segitiga XYZ:{luas:.2F}")
print(f"Keliling segitiga XYZ:{keliling:.2f}")
