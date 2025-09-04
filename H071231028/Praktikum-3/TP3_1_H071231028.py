n = int(input("Masukkan berapa banyak suku Fibonacci yang ingin dihasilkan: "))
a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b


    
