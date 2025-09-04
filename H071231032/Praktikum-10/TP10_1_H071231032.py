import os
import re
os.system('clear')

class Data:
    def __init__(self):
        pass

    def buat(self, nama, email, pswrd):
        self.nama = nama
        self.email = email
        self.pswrd = pswrd

    def ubah(self, namaBaru):
        self.nama = namaBaru

    def detail(self):
        print(f'Berikut data Anda :\nNama      : {self.nama}\nEmail     : {self.email}\nPassword  : {self.pswrd}')

    def hapus(self):
        del self.nama, self.email, self.pswrd
    
def saveData(namaFile, nama, email, pswrd):
    if os.path.exists(folder) == False:
        os.mkdir(folder)
    if os.path.exists(f"{folder}/{namaFile}.txt"):
        with open(f"{folder}/{namaFile}.txt", 'a') as fh:
            fh.write(f"\n| Nama      : {nama:<65}{'|':>0}\n| Email     : {email:<65}{'|':>0}\n| Password  : {pswrd:<65}{'|':>0}\n")
            fh.write('+' + '=' * 78 + f"{'+':>00}")
    else:
        with open(f"{folder}/{namaFile}.txt", 'a') as fh:
            fh.write('+' + '=' * 78 + f"{'+':>0}\n")
            fh.write(f"|{'DATA YANG TERSIMPAN':^78}{'|':>0}\n")
            fh.write('+' + '=' * 78 + f"{'+':>0}\n")
            fh.write(f"| Nama      : {nama:<65}{'|':>0}\n| Email     : {email:<65}{'|':>0}\n| Password  : {pswrd:<65}{'|':>0}\n")
            fh.write('+' + '=' * 78 + f"{'+':>00}")
    data.hapus()
    print('\nData Anda berhasil disimpan!')

def jumlahData(namaFile):
    x = 0
    if not os.path.exists(f"{folder}/{namaFile}.txt"):
        return f'\nFile {namaFile}.txt tidak ditemukan.'
    else:
        with open(f"{folder}/{namaFile}.txt") as fh:
            for i in fh:
                if '| Email     :' in i:
                    x += 1
    return f'\nJumlah data pada file {namaFile}.txt sebanyak {x}.'

data = Data()
folder = 'Dataset'

while True:
    print(f"{'=' * 60}\n" + "SELAMAT DATANG".center(60) + f"\n{'=' * 60}")
    opsi = input('Pilih opsi:\n1. Detail data Anda\n2. Buat data baru\n3. Ubah nama\n4. Save data pada file\n5. Jumlah data pada file\n6. Keluar\nOpsi Anda: ')
    print('=' * 60)
    if opsi == '1':
        try:
            data.detail()
        except AttributeError: print('Data saat ini kosong.')
        
    elif opsi == '2':
        while True:
            name = ''
            nama = input("Masukkan nama: ").title().replace(' ','')
            for i in nama:
                if i.isupper() and name != '':
                    name += ' '
                name += i
            if (name.replace(' ','').replace('.','')).isalpha() == False:
                print('\nNama harus huruf. Coba lagi!\n')
            elif len(name) == 0:
                print('\nNama tidak boleh kosong. Coba lagi!\n')
            else: break
        while True:
            eMail = input('\nMasukkan email: ')
            if not re.match(r'^[a-z\d.]+@student.unhas.ac.id$', eMail):
                print('\nEmail invalid. Coba lagi!')
            else: break
        while True:
            passWord = input('\nMasukkan password: ')
            if len(passWord) < 8 or len(passWord) > 20:
                print('\nPassword harus memiliki panjang 8-20 karakter')
            elif not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d\W]{1,}$', passWord):
                print('\nPassword Anda minimal memiliki huruf kapital, huruf kecil, dan angka. Coba lagi!')
            else: break
        data.buat(name, eMail, passWord)
        print('\nData Anda berhasil dibuat!')

    elif opsi == '3':
        try:
            if data.nama:
                while True:
                    namaBaru = input("Masukkan nama baru: ").title()
                    if (namaBaru.replace(' ','').replace('.','')).isalpha() == False: 
                        print('\nNama harus huruf!\n')
                    elif len(namaBaru) == 0:
                        print('\nNama tidak boleh kosong!\n')
                    else: print('\nNama berhasil diubah!'); break
                data.nama = namaBaru
        except AttributeError: print('Data saat ini kosong.')
    
    elif opsi == '4':
        try:
            if data.nama:
                saveData(input("Masukkan nama file (tanpa '.txt'): "), data.nama, data.email, data.pswrd)
        except AttributeError: print('Data saat ini kosong.')

    elif opsi == '5':
        print(jumlahData(input("Masukkan nama file (tanpa '.txt'): ")))
    
    elif opsi == '6':
        print(f"{'SAMPAI JUMPA':^60}" + '\n' + '='*60)
        break
    
    else: print('Opsi invalid. Coba lagi!')