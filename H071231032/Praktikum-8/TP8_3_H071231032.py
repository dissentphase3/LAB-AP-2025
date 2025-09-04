import re

userName = input('\nMasukkan username (minimal 5 karakter dan maksimal 20 karakter): ')
if not re.match(r'^[A-Za-z\d]{5,20}$', userName):
    print('\nUsername invalid. Registrasi gagal!')
    exit()

eMail = input('\nMasukkan email: ')
if not re.match(r'^[a-z\d.]+@[a-z]+\.(com|co\.id)$', eMail):
    print('Email invalid. Registrasi gagal!')
    exit()

passWord = input('\nMasukkan password (minimal 8 karakter): ')
if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$', passWord):
    print(f'\nRegistrasi berhasil! Selamat datang, {userName}\n')
else:
    print('Password invalid. Registrasi gagal!')