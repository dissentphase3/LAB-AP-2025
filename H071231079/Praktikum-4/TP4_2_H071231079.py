def palindrom(input_Palindrom: str)->str: #memberikan petunjuk input_Palindrom harus berupa string, dan fungsi akan mengembalikan string sebagai hasilnya
    frasa = input_Palindrom.lower().replace(" ", "")
    
    if frasa == frasa [::-1]: #[::-1] mencetak kebalikannya (dari huruf paling belakang hingga paling depan)
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
# Meminta Inputan
hasil = input(str("Masukkan Kata = "))
print(palindrom(hasil))  