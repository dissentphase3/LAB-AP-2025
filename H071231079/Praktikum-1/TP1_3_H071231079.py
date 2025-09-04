# Menghitung solusi persamaan kuadrat ax**2+bx+c=0

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

# Menghitung diskriminan
diskriminan = b**2 - 4*a*c

# Menghitung niai x
if a == 0:
    print("nlai a tidak boleh nol")
else:
    x1 = (-b + (diskriminan**0.5)) / (2*a)
    x2 = (-b - (diskriminan**0.5)) / (2*a)
    
print(f"x1 : {x1:.2f}")
print(f"x2 : {x2:.2f}")