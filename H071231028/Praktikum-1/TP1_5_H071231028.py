total_detik = int(input("Masukkan jumlah detik: "))

# Menghitung jumlah jam, menit, dan detik
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60


format_waktu = "{:02d}:{:02d}:{:02d}".format(jam, menit, detik)

# Menampilkan hasil
print("Waktu dalam format jam:menit:detik adalah:", format_waktu)
