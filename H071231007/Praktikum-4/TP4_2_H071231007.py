def cek_palindrom(kata):

    kata = kata.lower().replace(" ", "")
    kata_dibalik = kata[::-1] #[index_awal]:index_akhir:step(opsional)]
     
    if kata == kata_dibalik:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
kata = input("Masukkan kata: ")
print(cek_palindrom(kata))
