print("Konversi detik ke jam")
detik = int(input('Masukkan jumlah detik : '))

jam = detik // 3600
detik_sisa = detik % 3600
menit = detik_sisa // 60
detik_sisa = detik_sisa % 60

print(f"{jam:02d}:{menit:02d}:{detik_sisa:02d}")