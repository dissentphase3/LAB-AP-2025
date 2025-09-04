def stringBaru(kata):
    if len(kata) >= 3:
        newString = kata[0] + kata[len(inputString)//2] + kata[-1] #indeks
        return newString 
    else:
        return kata
    
inputString = input("Masukkan Kata : ")
print("String Baru : ", stringBaru(inputString))