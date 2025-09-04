a = input("Masukkan a: ").replace(" ", "")
b = input("Masukkan b: ").replace(" ", "")
b = b[::-1]
c = min(len(a), len(b))
hasil = ''.join(a[i] + b[i] for i in range(c))
hasil += a[c:] + b[c:]
print(hasil)