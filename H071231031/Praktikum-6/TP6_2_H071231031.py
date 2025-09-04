def input_array(Masukan):
    elemen = input(Masukan).split(' ')
    return [int(x) for x in elemen]

y = set()
arr1 = input_array("Input array ke-1 : ")

arr2 = input_array("Input array ke-2 : ")

for elemen in arr1:
    if elemen in arr2 and elemen not in y:
        y.add(elemen)

if len(y) > 0:
    print("Terdapat", len(y), "buah duplikat yaitu", f"{tuple (y)}")
else:
    print("Tidak ada duplikasi ditemukan.")