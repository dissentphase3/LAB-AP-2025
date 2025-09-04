def pembatas():
    print("=" * 50)

print("Selamat datang! untuk memulai silahkan input data anda\n")
data = dict()
nama = input("Input nama : "),
while True:
    umur = input("Masukkan umur : ")
    try:
        umur = int(umur)
        break
    except Exception:
        print("Invalid Input")
        continue
alamat = input("Input alamat : ")
data = {
    "nama" : nama,
    "umur" : umur,
    "alamat" : alamat
} 

while True:
    pembatas()
    print(f"Selamat Datang {data['nama']} silahkan pilih opsi")
    pembatas()
    print("1. Detail anda\n2. Ubah Nama \n3. Ubah Umur \n4. Ubah Alamat \n5. Keluar")
    pembatas()
    chc = int(input("Input Opsi : "))
    pembatas()
    

    match chc:
        case 1:
            print("Data anda adalah: ")
            for sub, info in data.items():
                print(f"{sub} : {info}")
        case 2:
            new = input("Silahkan Input nama baru : ")
            data["nama"] = new
            print("Data Anda sukses diperbarui")
        case 3:
            while True:

                new = input("Silahkan Input umur baru : ")
                try:
                    new = int(new)
                    data["umur"] = new
                    break
                except Exception:
                    print("Invalid Input")
                    continue
            print("Data Anda sukses diperbarui")
        case 4:
            new = input("Silahkan Input alamat baru : ")
            data["alamat"] = new
            print("Data Anda sukses diperbarui")
        case 5:
            print(f"Selamat tinggal {data['nama']}")
            break
        case _:
            print("Input anda tidak valid!")
            