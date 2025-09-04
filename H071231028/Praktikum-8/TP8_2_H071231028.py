import re

N = int(input())
hasil = []

for _ in range(N):
    baris = input().strip()
    if re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', baris):
        hasil.append("IPv4")
    elif re.match(r'^([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{1,4}$', baris):
        hasil.append("IPv6")
    else:
        hasil.append("Bukan IP Address")

for hasil1 in hasil:
    print(hasil1)