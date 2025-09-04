
while True:
    try:
        degrees = float(input("Masukkan sudut matahari atau bulan (0 ≤ M < 360): "))
        total_seconds = int( degrees * 240 + 21600 ) % 86400
        hours = total_seconds // 3600
        minutes = total_seconds % 3600 // 60
        seconds = total_seconds % 60

        if 6 <= hours < 12:
           print("Selamat Pagi")
        elif 12 <= hours < 15:
            print("Selamat Siang")
        elif 15 <= hours < 18:
            print("Selamat Sore")
        else:
            print("Selamat Malam")

        print(f"{hours:02}:{minutes:02}:{seconds:02}")
    except:
        print("end of file")
        break
    