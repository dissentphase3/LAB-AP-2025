kata = input("Masukkan kata: ")
hasil = len(kata)
if hasil > 3  :
    hasil = kata [0]  + kata [len(kata)//2] + kata [-1]

else :
    hasil = kata 
print (hasil)

