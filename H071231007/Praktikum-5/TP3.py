kata1 = input("masukkan kata pertana : ").lower().replace(" " , "")
kata2 = input("masukkan kata kedua : ").lower().replace(" " , "")
eror = 0

for i in kata1 :
    pertama = kata1.count(i)
    kedua = kata2.count(i)
    if pertama != kedua :
        eror += 1
if eror == 0 and len(kata1) == len(kata2) :
    print("True")
else :
    print ("False")

