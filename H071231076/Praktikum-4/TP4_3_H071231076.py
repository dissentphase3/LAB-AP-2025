def nilai_maksimal(*deret):
    nilai_terbesar = 0 #Nilai awal
    for angka in deret: #Melakukan looping untuk setiap angka dalam deret
        for j in angka :
            if j > nilai_terbesar:
                nilai_terbesar = j
    return nilai_terbesar

nilai = []
while True :
    input_deret = (input('Masukkan angka = '))
    if input_deret.lower() == 'selesai' :
        break
    nilai.append(int(input_deret))
print(nilai_maksimal(nilai))