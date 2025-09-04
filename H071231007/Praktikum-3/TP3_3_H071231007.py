while True:
    try:
        derajat = float(input("Masukan Posisi Matahari (Derajat) : "))
    except ValueError:
        print ("Invalid Input")
        exit()
    
    derajat *= 240
    jam = int(derajat // 3600)+6
    if jam >= 24:
        jam %= 24
    menit = int(derajat % 3600 // 60)
    derajat = int(derajat % 3600 % 60)
    hasil = (f"{jam:02}:{menit:02}:{derajat:02}")

    if jam >= 6 and jam < 12: 
       Waktu = "Pagi"
    elif jam >= 12  and jam < 15:
       Waktu = "Siang"
    elif jam >= 15 and jam < 18:
       Waktu = "Sore"
    else:Waktu = "Malam"

    print (f"Selamat {Waktu}\n{hasil}")
