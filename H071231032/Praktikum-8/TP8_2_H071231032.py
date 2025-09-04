import re

while True:
    try:
        n = int(input('\nMasukkan jumlah baris: '))
        if n <= 0:
            print('\nJumlah baris harus lebih dari nol!')
        else:
            break
    except ValueError:
        print('\nInputan jumlah baris harus integer!')
ip = [input('\nMasukkan IP Address: ') for _ in range(n)]

for i in ip:
    if re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$',i):
        print('\nIPv4')
    elif re.match(r'^([0-9a-f]{0,4}:){7}[0-9a-f]{1,4}$', i):
        print('\nIPv6')
    else:
        print('\nBukan IP Address')
