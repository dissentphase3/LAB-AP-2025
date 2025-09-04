def campur(s1, s2):
    nt1 = min( len(s1), len(s2))
    s3 = ""
    s2 = s2[::-1]

    for i in range(nt1):
        s3 += s1[i] + s2[i]
    s3 += s1[nt1:] + s2[nt1:]

    return s3
    

print("Hasil mixed =", campur(input("s1 = "), input("s2 = ")))


