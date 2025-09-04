try:
    def stringPermutation(kata):
        permutasi = []
        for i in range(len(kata)):
            kata = kata[-1] + kata[:-1] 
            permutasi.append(kata)

        return permutasi

    kata = input("Masukkan Kata = ")
     
    if kata.isdigit(): #Mengembalikan True jika inputan berupa angka
        raise TypeError # Memunculkan Pengecualian

    hasilPermutasi = stringPermutation(kata)

    for hasil in hasilPermutasi:
        print(hasil, end = " | ")

except TypeError:
    print("Error, Inputan harus berupa string")
except:
    print("Error, Inputan Valid")