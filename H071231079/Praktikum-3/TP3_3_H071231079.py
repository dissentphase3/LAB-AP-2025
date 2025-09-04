while True:
    try:
        M = float(input("Masukkan Derajat = "))
        detik = int(M * 240) #1 derajat sama dengan 240 detik atau 4 menit

        jam = detik // 3600 + 6 #Karena soal mengatakan 0 derajat berada di pukul 6
        if jam >= 24:
            jam  = jam % 24
        menit = detik % 3600 // 60
        n_detik = detik % 60

        if 6 <= jam < 11:
            print("Selamat Pagi")
        elif 11 <= jam < 15:
            print("Selamat Siang")
        elif 15 <= jam < 18:
            print("Selamat Sore")
        else:
            print("Selamat Malam")

        print(f"{jam:02}:{menit:02}:{n_detik:02}")

    except ValueError:
        print("End Of File")
        break