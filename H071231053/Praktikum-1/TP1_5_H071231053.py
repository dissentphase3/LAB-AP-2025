# Program Konversi waktu dari detik ke jam:menit:detik
detik = int(input("Masukkan jumlah detik: "))

# 3600 : 60 : 60 format jam : menit : detik (waktu)

jam = detik // 3600
detik_sisa = detik % 3600
menit = detik_sisa // 60
detik = detik_sisa % 60

format_waktu = "{:02d}:{:02d}:{:02d}".format(jam, menit, detik)

print("Waktu dalam format jam:menit:detik =", format_waktu)
