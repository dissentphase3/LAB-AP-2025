# Mencari Nilai X

a= float(input("a = "))

#Input a != 0 
while a == 0:
    print("input tidak valid!!( a !=0)")
    a = float(input("a= "))

b= float(input("b = "))
c= float(input("c = "))

#Nilai x1
x1 = (-b + ( b** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(f"x1 = {x1:.2f}")

#Nilai x2
x2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
print(f"x2 = {x2:.2f}")
