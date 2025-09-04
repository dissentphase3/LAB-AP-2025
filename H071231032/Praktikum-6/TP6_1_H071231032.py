print('\n\033[1mSelamat datang! Untuk memulai, silakan masukkan data Anda!\033[0m')
dataUser = {}
def namaUser(n):
    while True:
        try:
            if n == 1:
                nama = input('Masukkan nama Anda: ').title().lstrip()
            else:
                nama = input('Silakan masukkan nama baru Anda: ').title().lstrip()
            if (nama.replace(' ','').replace('.','')).isalpha() == False:
                raise Exception ('\nInputan nama Anda harus huruf!\n')
            elif len(nama) == 0:
                raise Warning ('\nInputan nama Anda tidak boleh kosong!\n')
            break
        except Warning as war:
            print(war)
        except Exception as ex:
            print(ex)
    return nama

def umurUser(n):
    while True:
        try:
            if n == 1:
                umur = int(input('Masukkan umur Anda: '))
            else:
                umur = int(input('Silakan masukkan umur baru Anda: '))
            if len(str(umur)) == 0:
                raise Exception ('\nInputan umur Anda tidak boleh kosong!\n')
            break
        except ValueError:
            print('\nInputan umur Anda harus integer!\n')
        except Exception as ex:
            print(ex)
    return umur

def alamatUser(n):
    while True:
        try:
            if n == 1:
                alamat = input('Masukkan alamat Anda: ').title().lstrip()
            else:
                alamat = input('Silakan masukkan alamat baru Anda: ').title().lstrip()
            if len(alamat) == 0:
                raise Exception ('\nInputan alamat Anda tidak boleh kosong!\n')
            break
        except Exception as ex:
            print(ex)
    return alamat
dataUser['Nama'], dataUser['Umur'], dataUser['Alamat'] = namaUser(1), umurUser(1), alamatUser(1)

while True:
    try:
        welcomeUser = f"Selamat datang, {dataUser['Nama']}! Silakan pilih opsi"
        print('\n'+'='*len(welcomeUser))
        print(f'\033[1m{welcomeUser}\033[0m')
        print('='*len(welcomeUser))
        print('\033[33m1.\033[0m Data detail Anda\n\033[33m2.\033[0m Ubah nama\n\033[33m3.\033[0m Ubah umur\n\033[33m4.\033[0m Ubah alamat\n\033[33m5.\033[0m Keluar')
        print('='*len(welcomeUser))
        opsi = input('Masukkan opsi pilihan Anda: \033[33m')
        print('\033[0m='*len(welcomeUser))
        opsi = int(opsi)

        if opsi > 5 or opsi < 1:
            raise Exception ('Opsi di luar jangkauan!')
        
        if opsi == 1:
            print(f"Berikut data detail Anda:\nNama: {dataUser['Nama']}\nUmur: {dataUser['Umur']} tahun\nAlamat: {dataUser['Alamat']}")

        elif opsi == 2:
            dataUser['Nama'] = namaUser(2)
            print('Data Anda sukses diperbarui.')

        elif opsi == 3:
            dataUser['Umur'] = umurUser(2)
            print('Data Anda sukses diperbarui.')

        elif opsi == 4:
            dataUser['Alamat'] = alamatUser(2)
            print('Data Anda sukses diperbarui.')

        else:
            print(f"\033[1mSelamat tinggal, {dataUser['Nama']}.\n")
            break

    except ValueError:
        print('\033[0mMasukkan opsi yang benar!')

    except Exception as ex:
        print(ex)