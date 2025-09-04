a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

x1 =(-b+(b**2 - 4*a*c)**0.5)/ (2*a)
x2 =(-b-(b**2 - 4*a*c)**0.5)/ (2*a)

   
print(f"Nilai dari x1 {x1:.2f}")
print(f"Nilai dari x2 {x2:.2f}")
