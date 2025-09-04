pengguna = {} 

print("Selamat datang untuk memulai silahkan input data anda")
pengguna["nama"] = input("Input nama: ")
pengguna["umur"] = input("Input umur: ")
pengguna["alamat"] = input("Input alamat: ")
while True:
    print("")
    x = len(f'Selamat datang {pengguna["nama"]} silahkan pilih opsi')
    print("="*x)
    print("Selamat datang", pengguna["nama"], "silahkan pilih opsi")
    print("="*x)
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("="*x)
    
    opsi = input("Input opsi: ")
    
    if opsi == "1":
        print("="*x)
        print("BIODATA ANDA")
        print("="*x)
        print("Nama:", pengguna["nama"])
        print("Umur:", pengguna["umur"])
        print("Alamat:", pengguna["alamat"])
    elif opsi == "2":
        pengguna["nama"] = input("Silahkan Input nama baru: ")
        print("Data anda sukses diperbarui")
    elif opsi == "3":
        while True:
            umur = input("Silahkan Input umur baru: ")
            if umur.isdigit():
                pengguna["umur"] = int(umur)
                break
            else:
                print("Umur harus berupa angka. Silakan coba lagi.")
        print("Data anda sukses diperbarui")
        
    elif opsi == "4":
        pengguna["alamat"] = input("Silahkan Input alamat baru: ")
        print("Data anda sukses diperbarui")
    elif opsi == "5":
        print("="*x)
        print("Selamat Tinggal", pengguna["nama"])
        break
    else:
        print("Silahkan pilih opsi 1-5 \n")

