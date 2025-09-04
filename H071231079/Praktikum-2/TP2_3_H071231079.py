g = input("Golongan = ").upper()
d = int(input("Daya = "))
p = int(input("Pemakaian = "))

match g, d:
    case "R1", 900:
        t = p * 1352
        print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
    case "R1", 1300:
        t = p * 1444.70
        print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
    case "R1", 2200:
        t = p * 1444.70
        print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
    case "R2", daya:
        if daya >=3500 and daya <=5500:
            t = p * 1699.53
            print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Invalid Input!")
    case "R3", daya:
        if daya >=6600:
            t = p * 1699.53
            print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Invalid Input!")
    case "B2", daya:
        if daya >=6600 and daya <=200000:
            t = p * 1444.70
            print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Invalid Input!")
    case "B3", daya:
        if daya >200000:
            t = p * 1114.74
            print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Invalid Input!")
    case "I3", daya:
        if daya >=200000:
            t = p * 1314.12
            print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Invalid Input!")
    case "P1", daya:
        if daya >=6600 and daya <=200000:
            t = p * 1523.28
            print(f"Jumlah Tagihan Anda : Rp, {round(t,2):,}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Invalid Input!")
    case _ :
        print("Invalid Input!")