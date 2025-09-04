# Input jumlah detik 
detik = int(input("Masukkan jumlah detik: "))

# Menghitung jam, menit, dan detik
jam = detik // 3600
sisa = detik % 3600
menit = sisa // 60
detik = sisa % 60

# Menampilkan hasil konversi dalam format 2 digit
format_waktu = f"{jam:02d}:{menit:02d}:{detik:02d}"
print(format_waktu)
