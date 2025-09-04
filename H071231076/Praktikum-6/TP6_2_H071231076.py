arr1 = set(map(int, input("Input array ke-1: ").split()))
arr2 = set(map(int, input("Input array ke-2: ").split()))

# duplicate = arr1.intersection(arr2)
duplicate = arr1 & arr2

if len(duplicate) > 1:
    print(f"Terdapat {len(duplicate)} buah duplikat yaitu {tuple(duplicate)}")
elif len(duplicate) == 1 :
    duplicate_list = list(duplicate)
    print(f"Terdapat 1 buah duplikat yaitu ({(duplicate_list[0])})")
else:
    print("Tidak ada duplikasi ditemukan.")