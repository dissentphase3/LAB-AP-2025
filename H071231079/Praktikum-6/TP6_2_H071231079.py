def duplikasi(array1, array2):
    duplikat = tuple(set(array1).intersection(set(array2)))
    if duplikat:
        if len(duplikat) == 1:
            return f"Terdapat {len(duplikat)} buah duplikat yaitu ({duplikat[0]})."
        else:
            return f"Terdapat {len(duplikat)} buah duplikat yaitu {duplikat}."
    else:
        return "Tidak ada duplikasi ditemukan."

arr1 = [int(elemen) for elemen in input("Input array ke-1 : ").split()]
arr2 = [int(elemen) for elemen in input("Input array ke-2 : ").split()]
print(duplikasi(arr1, arr2))