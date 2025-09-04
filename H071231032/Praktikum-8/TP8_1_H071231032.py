import re
x = input('\nMasukkan teks sebanyak 45 karakter (0 untuk selesai): ')
print('\nTrue') if re.match(r'^[02468A-z]{40}+[13579\s]{5}$', x) else print('\nFalse')
