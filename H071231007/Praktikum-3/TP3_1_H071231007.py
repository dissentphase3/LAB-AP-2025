N = int(input("Fibonaci : ")) 
if N == 0:  
    print (0)  
a,b = 0, 1  
for i in range(N): 
    print (a, end=" ") 
    a,b = b, a+b

