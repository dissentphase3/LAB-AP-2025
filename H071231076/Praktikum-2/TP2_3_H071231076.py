golongan = input("Golongan =").upper()
daya = int(input("Daya ="))
pemakaian = int(input("Pemakaian ="))

tagihan = 0

match (golongan, daya) :
    case ("R1",900) :
        tagihan = pemakaian * 1352
    case ("R1",1300) :
        tagihan = pemakaian * 1444.70
    case ("R1",2200) :
        tagihan = pemakaian * 1444.70
    case ("R2",_) if 3500 <= daya <=5500 :
        tagihan = pemakaian * 1699.53
    case ("R3",_) if daya >= 6600 :
        tagihan = pemakaian * 1699.53
    case ("B2",_) if  6600<= daya <= 200000 :
        tagihan = pemakaian * 1444.70
    case ("B3",_) if daya > 200000 :
        tagihan = pemakaian * 1114.74
    case ("I3",_) if daya >= 200000 :
        tagihan = pemakaian * 1314.12
    case ("P1",_) if  6600<= daya <=200000 :
        tagihan = pemakaian * 1523.28
    case _: 
        print("Data tidak valid")

if tagihan != 0 :
    print(f'Jumlah tagihan anda : Rp, {round(tagihan, 2):,}'.replace('.','|').replace(',','.').replace('|', ','))
