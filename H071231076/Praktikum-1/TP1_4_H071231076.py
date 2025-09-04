print("Pengujian Jenis Karakter")

karakter = input("\nKarakter :")

huruf_kapital = karakter >= 'A' and karakter <='Z'
huruf_kecil = karakter >= 'a' and karakter <='z'
angka = karakter >= '0' and karakter <='9'


print(f"Huruf Kapital?: {huruf_kapital}")
print(f"Huruf Kecil?: {huruf_kecil}")
print(f"Angka?: {angka}")