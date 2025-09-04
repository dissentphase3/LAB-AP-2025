#MENGHITUNG JUMLAH TAGIHAN
  
golongan_anda = input("golongan = ").upper()
daya_va = int(input ("daya = "))
pemakaian = int(input ("pemakaian = "))
tagihan=0
match golongan_anda :
    case "R1" :
        if daya_va == 900 :
            tagihan = round((pemakaian * 1352), 2)
        elif daya_va == 1300 :
            tagihan = round((pemakaian * 1444.70), 2)
        elif daya_va == 2200 :
            tagihan = round((pemakaian * 1444.70), 2)
        else :
            print ("data tidak valid")
    case "R2" :
        if 3500 <= daya_va <= 5500 :
            tagihan = round((pemakaian * 1699.53), 2)
        else :
            print ("data tidak valid")
    case "R3" :
        if daya_va >= 6600 :
            tagihan = round((pemakaian * 1699.53), 2)
        else :
            print ("data tidak valid")
    case "B2" :
        if 6600 <= daya_va <= 200000  :
            tagihan = round((pemakaian * 1444.70), 2)
        else :
            print ("data tidak valid")
    case "B3" :
        if daya_va > 200000 :
            tagihan = round((pemakaian * 1114.74), 2)
        else :
            print ("data tidak valid")
    case "I3" :
        if daya_va >= 200000 :
            tagihan = round((pemakaian * 1314.12), 2)
        else :
            print ("data tidak valid")
    case "P1" :
        if 6600 <= daya_va <= 200000 :
            tagihan = round((pemakaian * 1523.28), 2)
        else :
            print ("data tidak valid")
    case _:
        print ("invalid data")

if tagihan != 0:
    print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))