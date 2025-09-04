a = input('Masukkan kata: ')
print(a[0] + a[(len(a) // 2)] + a[-1]) if len(a) > 3 else print(a)