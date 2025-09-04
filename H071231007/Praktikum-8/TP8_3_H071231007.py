import re
username    = input("Masukkan Username : ")
pattern_usn = r"^[A-z0-9]{5,20}"
if re.fullmatch(pattern_usn, username):
    email       = input("Masukkan Email    : ")
    pattern_email = r"^[.a-z]+(\d{2,})?@[a-z]+\.(com|co\.id)"
    if re.fullmatch(pattern_email, email):
        password    = input("Masukkan Password : ")
        pattern_pw  = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[\d])[A-Za-z0-9]{8,}"
        if re.fullmatch(pattern_pw, password):
            print(f"Registrasi Berhasil!, Selamat datang, {username}!")
        else:
            print("Password anda tidak valid")
    else:
        print("Email yang dimasukkan tidak valid!")
else:
    print("Username yang dimasukkan tidak valid!")

