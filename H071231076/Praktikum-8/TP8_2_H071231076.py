import re
n = int(input())
list_ip = []
for i in range(n) :
    ip_address = input()
    list_ip.append(ip_address)
for i in range(len(list_ip)) :
    if len(list_ip[i]) <= 500 :
        ipv4 = re.match(r'^(25[0-5]|2[0-4]\d|1\d\d|[0-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[0-9]?\d)){3}$',list_ip[i])
        ipv6 = re.match(r'^([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{1,4}$',list_ip[i])
        if ipv4 :
            print('IPv4')
        elif ipv6 :
            print('IPv6')
        else :
            print('Bukan IP Address')