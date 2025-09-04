print("Selamat datang untuk memulai silahkan input data anda")

data = {
    'Nama': '',
    'Umur': '',
    'Alamat': ''
}
while True :
    try : 
        data['Nama'] = input("Input nama: ")
        if not data['Nama'].replace(".", "").replace(" ", "").isalpha() :
            print("Nama harus berupa huruf")    
        else :
            break
    except :
        pass
while True : 
    try :
        data['Umur'] = int(input("Input umur: "))
        break
    except ValueError :
        print("Umur harus berupa angka")

data['Alamat'] = input("Input alamat: ")
print()

while True:
    print("="*50)
    print("Selamat datang", data['Nama'], "silahkan pilih opsi")
    print("="*50)
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("="*50)

    opsi = input("Input opsi: ")

    if opsi == '1':
        print("="*50)
        print("Data anda adalah")
        print("Nama:", data['Nama'])
        print("Umur:", data['Umur'])
        print("Alamat:", data['Alamat'])
        print("="*50)
        input()
    elif opsi == '2':
        while True :
            try : 
                data['Nama'] = input("Input nama: ")
                if not data['Nama'].replace(".", "").replace(" ", "").isalpha() :
                    print("Nama harus berupa huruf")    
                else :
                    break
            except :
                pass
        print("Data anda sukses diperbarui")
        input()
    elif opsi == '3':
        while True :
            try : 
                data['Umur'] = int(input("Silahkan Input umur baru: "))
                print("Data anda sukses diperbarui")
                break
            except ValueError :
                print("Umur harus berupa angka")
        input()
    elif opsi == '4':
        data['Alamat'] = input("Silahkan Input alamat baru: ")
        print("Data anda sukses diperbarui")
        input()
    elif opsi == '5':
        print("="*50)
        print("Selamat Tinggal", data['Nama'])
        break
    else:
        print("Opsi tidak valid. Silahkan coba lagi.")