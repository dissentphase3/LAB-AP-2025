import re

def validUser(username):
    pattern = r'^[a-zA-Z0-9]{5,20}$'
    match = re.search(pattern, username)
    return match

def validEmail(email):
    pattern = r'^[a-z0-9.]+@[a-z]+\.(com|co\.id)$'
    match = re.search(pattern, email)
    return match

def validPass(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{8,}$' #positive lockahead
    match = re.search(pattern, password)
    return match
    
username = input("Masukkan username  : ")
if validUser(username):
    email = input("Masukkan email     : ")
    if validEmail(email):
        password = input("Masukkann password : ")
        if validPass(password):
            print(f"Registrasi berhasil! Selamat datang, {username}")
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal!")
    else:
       print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
else:
      print("\nInputan Username tidak valid dalam sistem. Registrasi gagal!")

#Hengkerprotzy82372838232
