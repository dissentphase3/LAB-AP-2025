def anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        return False
    
    for i in kata1:
        if kata1.count(i) != kata2.count(i): #count untuk menghitung kemunculan elemen tertentu dalam iterasi (daftar data)
            return False
    return True

kata1 = input("Masukkan kata pertama : ").replace(" ", "").lower()
kata2 = input("Masukkan kata kedua : ").replace(" ", "").lower()
print(anagram(kata1, kata2))    