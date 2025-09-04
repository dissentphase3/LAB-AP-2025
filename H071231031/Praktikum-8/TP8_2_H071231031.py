import re

def IPv4(teks):
    pattern =  (r"^(25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3}$")
    match = re.match(pattern, teks)

    if match:
        return True
    else:
        return False

def IPv6(teks):
    pattern = (r'^(?:[0-9a-f]{0,4}:){7}[0-9a-f]{1,4}$')
    match = re.match(pattern, teks)

    return True if match else False

def IP_match(teks):
    for _ in teks:
        if IPv4(_):
            print('IPv4')
        elif IPv6(_):
            print('IPv6')
        else:
            print('Bukan IP address')

n = int(input('Baris: '))

teks1 = []
for _ in range (n):
    teks1.append(input())

print()
IP_match(teks1)