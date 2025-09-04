var = input("Masukkan kata = ")
mid = len(var)//2

if len(var)<3:
    print(var)       
else: 
    print(var[0]+var[mid]+var[-1])
