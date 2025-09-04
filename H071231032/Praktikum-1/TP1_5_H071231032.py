# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Pekan Pertama Praktikum Algoritma dan Pemrograman

print("\nSoal nomor lima: Konversi Detik ke Dalam Format jam:menit:detik\n")

dtk = int(input("Masukkan jumlah detik: "))
jam = dtk // 3600
detikSisa = dtk % 3600
menit = detikSisa // 60
detik = detikSisa % 60

print(f"\n{jam:02}:{menit:02}:{detik:02}\n")