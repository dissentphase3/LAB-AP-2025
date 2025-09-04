s1 = input("s1 = ").replace(" ","")
s2 = input("s2 = ")[::-1].replace(" ","")
s3 = (min(len(s1),len(s2))) #Mengambil nilai terpendek dari dua variabel
hasil = ""

for i in range (s3) :
    hasil = hasil + s1[i] + s2[i]

if len(s1) > len(s2):
    hasil = hasil + s1[s3:]
else:
    hasil = hasil + s2[s3:]

print(f'Hasil mixed = "{hasil}"')