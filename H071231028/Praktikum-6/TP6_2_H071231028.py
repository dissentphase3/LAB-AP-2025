x = input("Input array ke-1: ").split()
y = input("Input array ke-2: ").split()
duplikat = set(int(jumlah) for jumlah in x) & set(int(jumlah) for jumlah in y)
if len(duplikat) > 0:
    print("Terdapat {} buah duplikat yaitu {}".format(len(duplikat), str(list(duplikat)).replace('[', '(').replace(']', ')')))
else:
    print("Tidak ada duplikasi ditemukan.")