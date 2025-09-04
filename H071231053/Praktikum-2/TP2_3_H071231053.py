gol = input("Golongan: ").upper()
daya = int(input("Daya (VA): "))
pemakaian = int(input("Pemakaian (kWh): "))
tarif_per_kWh = None

if gol == "R1":
    if daya == 900:
        tarif_per_kWh = 1352
    elif daya == 1300:
        tarif_per_kWh = 1444.70
    elif daya == 2200:
        tarif_per_kWh = 1444.70
elif gol == "R2" and 3500 <= daya <= 5500:
    tarif_per_kWh = 1699.53
elif gol == "R3" and daya > 6600:
    tarif_per_kWh = 1699.53
elif gol == "B2" and (6600 <= daya <= 200000):
    tarif_per_kWh = 1444.7 
elif gol == "B3" and daya > 200000:
    tarif_per_kWh = 1114.74  
elif gol == "I3" and daya > 200000:
    tarif_per_kWh = 1314.12  
elif gol == "P1" and (6600 <= daya <= 200000):
    tarif_per_kWh = 1523.28  

if tarif_per_kWh is None:
    print("Data tidak valid")
    exit()
else:
    total = round((pemakaian * tarif_per_kWh),2)
    format_total = f"Rp, {total:,}".replace('.', '|').replace(',', '.').replace('|', ',')
    print(f"Pemakaian = Jumlah tagihan anda sebesar {format_total}")
