print("Masukkan kalimat pertama")
T1 = str(input())
print("Masukkan kalimat kedua")
T2 = str(input())

T1 = T1.replace(" ", "").lower()
T2 = T2.replace(" ", "").lower()
K1 = {}
for i in T1:
    if i in K1:
        K1[i] += 1
    else:
        K1[i] = 1
print(K1)
K2 = {}
for i in T2:
    if i in K2:
        K2[i] += 1
    else:
        K2[i] = 1
print(K2)

if K1 == K2:
    print(True)
else:
    print(False)
