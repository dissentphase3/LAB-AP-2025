print('##  Konversi Suhu  ##')

celc = float(input('Input suhu celsius: '))
 
fahr = int((9/5 * celc) + 32)
kelv = int(celc + 273.15)
ream = int(celc * (4/5))
 
print(celc,'derajat Celsius =',fahr,'derajat Fahrenheit')
print(celc,'derajat Celsius =',kelv,'derajat Kelvin')
print(celc,'derajat Celsius =',ream,'derajat Reamur')
