def kata_baru(kata):
    if len(kata) < 3:
        return kata
    return kata[0] + kata[len(kata) // 2] + kata[-1]

campur = input("Masukkan kata: ")
hasil = kata_baru(campur)
print("Hasil:", hasil)


