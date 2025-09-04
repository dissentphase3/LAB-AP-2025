def terbesar(*x):
    terbesar = 0
    for i in x:
        for j in i:
            if j > terbesar:
                terbesar = j
    return terbesar

# nilai = list(map(int,input("Masukkan input: ").rstrip().split()))
# print("angka terbesar = ",terbesar(nilai))
tes=[]
while True:
    nilai = input("masukkan input= ")
    if nilai.lower() == "selesai":
        break
    else:
        tes.append(int(nilai))
print(terbesar(tes))

    