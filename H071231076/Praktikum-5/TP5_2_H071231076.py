kalimat = input("Masukkan kata = " ).replace(" ","")
    
karakter_satu = kalimat[0]
karakter_dua = kalimat[len(kalimat)//2]
karakter_tiga = kalimat[-1]

hasil = karakter_satu + karakter_dua + karakter_tiga

if len(kalimat) <3 :
    print(kalimat)
else :
    print(hasil)