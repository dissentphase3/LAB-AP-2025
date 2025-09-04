import re
def is_valid_username(username):
    return re.match(r'^[A-Za-z0-9]{5,20}', username)
def is_valid_email(email):
    return re.match(r'^[a-z.]+(\d{2,})?@[a-z]+\.(com|co\.id)$', email)
def is_valid_password(password):
    return re.match(r'^[A-Z]*[a-z]*\d*[A-Za-z\d]{8,}', password)
username = input('Masukkan username: ')
if is_valid_username(username):
    email = input('Masukkan email: ')
    if is_valid_email(email):
        password = input('Masukkan password: ')
        if is_valid_password(password):
            print('\nRegistrasi berhasil! Selamat datang,', username)
        else:
            print('\nPassword yang kamu input sangat beresiko. Registrasi gagal.')
    else:
        print('\nEmail yang kamu input tidak valid. Registrasi gagal!')
else:
   print('\nInputan username tidak valid dalam sistem. Registrasi gagal!')