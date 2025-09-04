kata_pertama = input("Masukkan kata pertama : ").replace(" ","").lower()
kata_kedua = input("Masukkan kata kedua : ").replace(" ","").lower()

for karakter in kata_pertama :
    hasil1 = kata_pertama.count(karakter)
    hasil2 = kata_kedua.count(karakter)

    if hasil1 == hasil2 :
        continue
    else :
        print("False")
        break

else : # Dieksekusi jika loop selesai tanpa pernyataan break
    print("True")