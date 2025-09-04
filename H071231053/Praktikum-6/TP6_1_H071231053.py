dictkosong =  {}
print("Selamat datang, untuk memulai silakan input data anda")
dictkosong["nama"] = str(input("Input nama : "))
dictkosong["umur"] = int(input("Input umur : "))
dictkosong["alamat"] = str(input("Input alamat : "))
while True:
    print(f"""
=======================================================
Selamat datang {dictkosong["nama"]} silahkan pilih opsi
=======================================================
1. Detail anda 
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar
=============================================================""")
    pilihan = int(input("input opsi = "))  
    
    match pilihan:
        case 1:
            print(f"""=============================================================
        Data anda adalah 
        Nama : {dictkosong["nama"]}
        Umur : {dictkosong["umur"]}
        Alamat : {dictkosong["alamat"]}
            """)

        case 2:
            dictkosong["nama"] = input ("Silahkan input nama baru : ")
            print("Data anda telah diperbarui")
        case 3:
            dictkosong["umur"] = input ("Silahkan input umur baru : ")
            print("Data anda telah diperbarui")
        case 4:
            dictkosong["alamat"] = input ("Silahkan input alamat baru : ")
            print("Data anda telah diperbarui")
        case 5: 
            print(f"Selamat tinggal {dictkosong['nama']}!")
            break
        case _:
            print("pilihan tidak tersedia")