try :
    while True :
        M = float(input())
        total_detik = int((M / 360) * 24 * 3600)

        jam = (total_detik // 3600 + 6) % 24
        menit = (total_detik % 3600) // 60
        detik = total_detik % 60

        if 6 <= jam < 12:
            waktu = "Selamat Pagi"
        elif 12 <= jam < 15:
            waktu = "Selamat Siang"
        elif 15 <= jam < 18:
            waktu = "Selamat Sore"
        else:
            waktu = "Selamat Malam"
        print(waktu)
        print(f"{jam:02d}:{menit:02d}:{detik:02d}")
except ValueError :
    print("Invalid")