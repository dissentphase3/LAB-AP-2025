import re

def IPv4(teks):
    pattern = r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    match = re.search(pattern, teks)
    if match:
        return True
    else:
        return False
    
def IPv6(teks):
    pattern = r'^([A-Fa-f0-9]{0,4}:){7}([A-Za-z0-9]{1,4})$' 
    match = re.search(pattern, teks)
    if match:
        return True
    else:
        return False

n = input("Masukkan N Baris : ")
while not n.isdigit():
    print("Inputan invalid!. Silakan coba lagi.")
    n = input("Masukkan N Baris : ")

listid = []
for i in range(int(n)):
    listid.append(input())

for i in listid:
    if IPv4(i):
        print("IPv4")
    elif IPv6(i):
        print("IPv6")
    else:
        print("Bukan IP Address")

#213.214.111.564
#444.444.444.444 not an ip address
#1050:0:0a:0:5:600:300c:326b

#121.203.197.20
#2001:0db8:0000:0000:0000:ff00:0042:8329