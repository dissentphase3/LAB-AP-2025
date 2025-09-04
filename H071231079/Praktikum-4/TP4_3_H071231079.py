def maksimum(*daftar_angka):
    terbesar = 0

    for i in daftar_angka:
        for j in i: 
            if j > terbesar:
                terbesar = j
    
    return terbesar

daftarAngka = []
while True:
    try:
        input_string = input("Masukkan Angka = ")
        
        if input_string.lower() == 'selesai':
            break

        angka = int(input_string)
        daftarAngka.append(angka)
        
    except ValueError:
        print("Inputan harus berupa angka!")

print("Angka di dalam daftar = ", daftarAngka)

hasil = maksimum(daftarAngka)
print(">>", hasil)