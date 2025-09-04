def permutasiKata(kata):
    for karakter in kata:
        if not ('a' <= karakter <= 'z' or 'A' <= karakter <= 'Z'):
            print("Masukkan harus berupa huruf saja.")
            return
    permutasi = [kata[-i:] + kata[:-i] + " | " for i in range(1, len(kata) + 1)]
    hasil = ""
    for p in permutasi:
        hasil += p
    print(hasil)
kata_input = input("Masukkan kata: ")
permutasiKata(kata_input)
