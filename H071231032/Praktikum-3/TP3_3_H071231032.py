# Muhammad Qaffal Al Fifaiz | H071231032 | Tugas Pekan Ketiga
while True:
    try:
        M = float(input('Masukkan derajat: '))
        if 0 <= M:
            detikSehari = 24 * 3600 
            detikDerajat = (M / 360) * detikSehari
            jam = int(((detikDerajat // 3600) + 6) % 24)
            sisaDetik = detikDerajat % 3600
            menit = int(sisaDetik // 60)
            detik = int(sisaDetik % 60 + 0.5)

            if 5 <= jam < 11:
                hari = 'Pagi'
            elif 11 <= jam < 15:
                hari = 'Siang'
            elif 15 <= jam < 18:
                hari = 'Sore'
            elif 18 <= jam < 19:
                hari = 'Senja'
            else:
                hari = 'Malam'
            print(f"\nSelamat {hari}")
            print(f"{jam:02}:{menit:02}:{detik:02}\n")
        else:
            print("\nInput di luar jangkauan.\n")
            
    except ValueError:
        print("\nInputan harus berupa angka.\n")
        break