print('menghitung luas permukaan dan keliling segitiga')

a = float(input('masukkan nilai a : '))
b = float(input('masukkan nilai b : '))

luas = 1/2*(a*b)
c = (a**2+b**2)**0.5
keliling=a+b+c

print(f'luas permukaan :{luas: .2f}')
print(f'keliling       :{keliling: .2f}')

      