p = int(input())
u = int(input())
if u < p:
    print("Uang tidak cukup")
else:
    k = u - p
    uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    for n in uang:
        j = k // n
    k %= n
    print(f"{j} uang sejumlah Rp. {n}")