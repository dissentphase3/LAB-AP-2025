def kata(x1,x2) :
    hasil = ""
    pendek = min(len(x1),len(x2))
    x2 = x2[::-1]


    for i in range(pendek) :
        hasil += x1[i] + x2 [i]
    hasil += x1[pendek: ] + x2[pendek: ]
    return hasil
x1 = input("masukkan kata pertama : ")
x2 = input("Masukkan kata kedua : ")
print(kata(x1,x2))

