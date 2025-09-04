print("Konversi Detik ke Jam\n")

totaldetik = int(input("Masukkan detik: "))

jam = totaldetik // 3600
sisa_detik = totaldetik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

format_waktu = "{:02d}:{:02d}:{:02d}".format(jam,menit,detik)

print("Detik sama dengan", format_waktu)
 