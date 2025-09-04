def anagram(kata1, kata2):
    kesalahan = 0
    
    for word in kata1:
        nt1 = kata1.count(word)
        nt2 = kata2.count(word)
        if nt1 != nt2 :
            kesalahan += 1

    if kesalahan == 0 and len(kata1) == len(kata2):
        return True
    else:
        return False
    
if anagram(input("Masukkan kata pertama: ").replace(" ", "").lower(), input("Masukkan kata kedua: ").replace(" ", "").lower()): 
    print("True")
else:
    print("False")


