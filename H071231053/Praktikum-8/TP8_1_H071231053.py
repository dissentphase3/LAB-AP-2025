import re
x = input("Masukkan inputan: ")
pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}"
y = re.fullmatch(pattern,x)
if y :
    print(True)
else:
    print(False)

