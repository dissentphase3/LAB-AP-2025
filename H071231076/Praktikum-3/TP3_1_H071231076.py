n = int(input(''))

a = 0
b = 1

if n <= 1:
    print(a)
else:
    print(a,b,end=' ')
    for x in range(2,n):
        c = a+b
        print(c, end=" ")
        a = b
        b = c