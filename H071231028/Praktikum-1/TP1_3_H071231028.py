a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

 
#Menghitung Argumen
x1 =(-b+(b**2 - 4*a*c)**0.5)/ (2*a)
x2 =(-b-(b**2 - 4*a*c)**0.5)/ (2*a)

print(f"nilai dari x1 adalah {x1:.2f}")
print(f"nilai dari x2 adalah {x2:.2f}")
