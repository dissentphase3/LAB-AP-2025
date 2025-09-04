dataDetail = {}

print("Selamat datang! Untuk memulai, silahkan input data anda : ")
nama = input("Input Nama : ")
while not nama.replace(".", "").replace(" ", "").isalpha():
    print("Nama harus berupa huruf. Silakan coba lagi.")
    nama = input("Input Nama : ")
umur = input("Input Umur : ")
while not umur.isdigit():
    print("Umur harus berupa angka. Silakan coba lagi.")
    umur = input("Input Umur : ")
alamat = input("Input Alamat : ")

dataDetail["Nama"] = nama
dataDetail["Umur"] = umur
dataDetail["Alamat"] = alamat

while True:
    print("=" * 60)
    print(f"Hai, Selamat datang {dataDetail['Nama']}! Silahkan pilih opsi di bawah!")
    print("1. Detail Anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar")
    print("=" * 60)

    pilihanOpsi = input("Input Opsi : ")

    if pilihanOpsi == "1" :
        print("=" * 60 )
        print("Data anda adalah : ")
        print("Nama   : ", dataDetail["Nama"])
        print("Umur   : ", dataDetail["Umur"])
        print("Alamat : ", dataDetail["Alamat"])
        print("=" * 60)
    
    elif pilihanOpsi == "2":
        while True:
            namaBaru = input("Silahkan masukkan nama baru anda : ")
            if namaBaru.replace(".", "").replace(" ", "").isalpha():
                dataDetail["Nama"] = namaBaru
                print("Data anda sukses diperbarui!")
                print(" ")
                break
            else:
                print("Inputan nama harus berupa huruf!")

    elif pilihanOpsi == "3":
        while True:
            umurBaru = input("Silahkan masukkan umur baru anda : ")
            if umurBaru.isdigit():
                dataDetail["Umur"] = umurBaru
                print("Data anda sukses diperbarui!")
                print(" ")
                break
            else:
                print("Inputan umur harus berupa angka!")

    elif pilihanOpsi == "4" :
        alamatBaru = input("Silahkan masukkan alamat baru anda : ")
        dataDetail["Alamat"] = alamatBaru
        print("Data anda sukses diperbarui!")
        print(" ")

    elif pilihanOpsi == "5":
        print("=" * 60)
        print(f"Bye, Selamat tinggal {dataDetail['Nama']}!")
        break

    else:
        print("Invalid Input!")