def mix_strings(s1, s2):
    s2 = s2[::-1]
    s3 = ""
    panjangMin = min(len(s1), len(s2)) #hanya mengambil nilai minimun diantara keduanya

    for i in range(panjangMin):
        s3 += s1[i] + s2[i]

    s3 += s1[panjangMin:] + s2[panjangMin:]
    return s3

s1 = input("Masukkan s1 : ").replace(" ", "")
s2 = input("Masukkan s2 : ").replace(" ", "")
print(mix_strings(s1, s2))