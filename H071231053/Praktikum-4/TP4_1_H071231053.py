def stringPermutation(kata):
    try:
        if len(kata) <= 1:
            return kata

        hasil_permutasi = []
        for i in range(len(kata)):
            kata = kata[-1:] + kata[:-1]
            hasil_permutasi.append(kata)

        return ' | '.join(hasil_permutasi) + ' |'

    except TypeError as msg:
        return f'Terjadi kesalahan karena {msg}'

word = input("Masukkan kata: ")
if word.isdigit(): 
    quit()

hasil = stringPermutation(word)
print(hasil)

