import re

ipv4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
ipv6 = r"^([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{1,4}$"
x = []
a = int(input())
for i in range (a):
    i = input()
    x.append(i)
print("")
for i in x :
    if re.match(ipv4,i):
        print("ipv4")
    elif re.match(ipv6,i):
        print("ipv6")
    else :
        print("Bukan IP address")