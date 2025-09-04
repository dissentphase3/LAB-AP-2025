import re

stringInput = input("Masukkan String Inputan : ")
pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$' 
if re.search(pattern, stringInput):
    print("True")
else:
    print("False")

#2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
#x42002v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779