# Mengambil input dari pengguna
input_char = input("Masukkan sebuah karakter: ")
is_upper = input_char>='A' and input_char<='Z'
is_lower = input_char>='a' and input_char<='z'
is_digit = input_char>='0' and input_char<='9'

# Menampilkan hasil
print(f'Huruf kapital: {is_upper}')
print(f'Huruf kecil: {is_lower}')
print(f'Angka: {is_digit}')

