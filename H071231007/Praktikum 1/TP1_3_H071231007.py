#Tugas 3 Persamaan Kuadrat
a = float(input("Input a = "))
if a == 0:
    print("Input a tidak boleh 0!")
    exit()
b = float(input("Input b = "))
c = float(input("Input C = "))

a1 = b**2
a2 = 4*a*c
a3 = 2*a
#Rumus Persamaan Kuadrat
x1 =(- b + (a1 - a2)**0.5)/(a3)
x2 =(- b - (a1 - a2)**0.5)/(a3)

print(f'x1= {x1: .2f}')
print(f'x2= {x2: .2f}')

