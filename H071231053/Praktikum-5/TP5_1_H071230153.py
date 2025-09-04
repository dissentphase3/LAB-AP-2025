def pergabungan(kata1, kata2):
    var = ''
    kata2 = kata2[::-1]
    panjang_kata = min(len(kata1), len(kata2))

    for i in range(panjang_kata):
        var += kata1[i] + kata2[i]

    var += kata1[panjang_kata:] + kata2[panjang_kata:]
    return var

kata1 = input("Masukkan input : ")
kata2 = input("Masukkan input : ")
output = pergabungan(kata1,kata2)
print(output)
