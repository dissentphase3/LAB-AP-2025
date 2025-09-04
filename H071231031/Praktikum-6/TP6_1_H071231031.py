data = {}

def is_huruf(input_text):
    return all(char.isalpha() or char.isspace() or char == '.' for char in input_text)

def is_angka(input_text):
    return all(char.isdigit() for char in input_text)

print("Selamat datang! Silakan masukkan data Anda.")

while True:
    nama = input("Nama (huruf saja): ")
    if is_huruf(nama):
        data["nama"] = nama
        break
    else:
        print("Nama hanya boleh mengandung huruf.")

while True:
    umur = input("Umur (angka saja): ")
    if is_angka(umur):
        data["umur"] = umur
        break
    else:
        print("Umur hanya boleh mengandung angka.")

alamat = input("Alamat: ")
data["alamat"] = alamat

while True:
    print("=" * 50)
    print("Silakan pilih opsi:")
    print("=" * 50)
    print("1. Tampilkan data")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("=" * 50)

    pilihan = input("Input opsi: ")
    
    if pilihan == "1":
        print("=" * 50)
        print("Data Anda:")
        print(f"Nama: {data.get('nama')}")
        print(f"Umur: {data.get('umur')}")
        print(f"Alamat: {data.get('alamat')}")
            
    elif pilihan == "2":
        while True:
            nama_baru = input("Silakan input nama baru (huruf saja): ")
            if is_huruf(nama_baru):
                data["nama"] = nama_baru
                print("Data Anda sukses diperbarui!")
                break
            else:
                print("Nama hanya boleh mengandung huruf.")
        
    elif pilihan == "3":
        while True:
            umur_baru = input("Silakan input umur baru (angka saja): ")
            if is_angka(umur_baru):
                data["umur"] = umur_baru
                print("Data Anda sukses diperbarui!")
                break
            else:
                print("Umur hanya boleh mengandung angka.")
        
    elif pilihan == "4":
        alamat_baru = input("Silakan input alamat baru: ")
        data["alamat"] = alamat_baru
        
    elif pilihan == "5":
        print(f"Selamat tinggal {data.get('nama', 'Pengguna')}")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")