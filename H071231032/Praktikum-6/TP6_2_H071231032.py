while True:
    try:
        arr1 = [int(i) for i in input('\nMasukkan angka untuk \033[35marray ke-1\033[0m (pisahkan dengan spasi): \033[33m').split(' ')]
        arr2 = [int(i) for i in input('\033[0mMasukkan angka untuk \033[35marray ke-2\033[0m (pisahkan dengan spasi): \033[33m').split(' ')]
        break

    except ValueError:
        print('\n\033[0mInputan invalid.')
arrDuplikat = set()

for i in arr1:
    if i in arr2 and i not in arrDuplikat:
        arrDuplikat.add(i)

x = str(arrDuplikat).replace('{','').replace('}','')

if len(arrDuplikat) == 0:
    print('\n\033[0mTidak ditemukan duplikasi.\n')
else:
    print(f"\n\033[0mTerdapat \033[35m{len(arrDuplikat)} \033[0mbuah duplikat, yaitu (\033[33m{x}\033[0m)\n")