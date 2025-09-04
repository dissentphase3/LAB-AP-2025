while True:
    try:
        d = float(input())
        j = int((d / 360) * 24)
        m = int(((d / 360) * 24 - j) * 60)
        s = int(((d / 360) * 24 - j) * 3600 + 0.5) % 60
        j = (j + 6) % 24
        p = ""
        if j >= 6 and j < 12:
            p = "Selamat Pagi"
        elif j >= 12 and j < 15:
            p = "Selamat Siang"
        elif j >= 15 and j < 18:
            p = "Selamat Sore"
        else:
            p = "Selamat Malam"
        print(p)
        print(f"{j:02d}:{m:02d}:{s:02d}")
    except ValueError:
        print("invalid")
        break