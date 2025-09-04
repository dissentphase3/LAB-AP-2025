n = int(input("Masukkan nilai n : "))
s1 = 0
s2 = 1
if n == 1:
    print(s1)
elif n <= 0:
    print("Bukan Fibonacci!")
else:
    print(s1, s2, end = " ")
    for i in range(2, n):
        s3 = s1 + s2
        s1, s2 = s2, s3
        print(s3, end = " ")