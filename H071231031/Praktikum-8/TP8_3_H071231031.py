import re
def is_valid(string, pattern):
     return re.search(pattern, string)

username = input("Masukkan username: ")
if not is_valid(username, r"^[A-Za-z0-9]{5,20}$"): 
     print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")
     exit()

email = input("Masukkan email: ")
if not is_valid(email, r"^[a-z0-9.*]+@[a-z]+\.(com|co\.id)$"):
    print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
    exit()

password = input("Masukkan password: ")
if not is_valid(password, r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9]{8,}$"):
    print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    exit()
print(f"\nRegistrasi berhasil! Halo, {username}")