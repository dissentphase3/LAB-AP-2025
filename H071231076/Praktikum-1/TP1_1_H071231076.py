x = float(input("Panjang sisi x:"))
y = float(input("Panjang sisi y:"))
z= (x**2 + y**2)**0.5

s= (x + y + z) / 2
luas = (s* (s-x)* (s-y)* (s-z))**0.5
keliling= x + y + z

print(f" luas segitiga xyz adalah {luas:.2f}")
print(f" luas keliling xyz adalah {keliling:.2f}")

