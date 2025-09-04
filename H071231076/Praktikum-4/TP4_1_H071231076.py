def permutasiString(word):
    try: 
        permutasi = " " #Nilai awal
        for i in range(len(word)):
            rotated_word = word[-1] + word[:-1] #Membuat efek rotating karakter terakhir ke depan
            permutasi = permutasi + rotated_word + ' | ' #Menambahkan sebuah permutasi yang telah dimodifikasi oleh rotated_word
            word = rotated_word #Memperbarui kata dengan nilai rotated_word untuk melakukan permutasi berikutnya
        return permutasi
    except TypeError:
        pass
    
word = input()

if word.isdigit():
    print("Error")
else:
    print(f'stringPermutation("{word}")')
    print(permutasiString(word))