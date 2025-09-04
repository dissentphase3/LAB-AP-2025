array1 = set(map(int, input('Input array ke-1: ').split(' ')))
array2 = set(map(int, input('Input array ke-2: ').split(' ')))

duplikat = tuple(array1 & array2)
jumlah = len(duplikat)

if jumlah == 0:
    print(f'tidak ada duplikasi ditemukan.')
elif jumlah == 1:
    print(f'Terdapat {jumlah} buah duplikat yaitu ({duplikat[0]})')
else:
    print(f'Terdapat {jumlah} buah duplikat yaitu {duplikat}')