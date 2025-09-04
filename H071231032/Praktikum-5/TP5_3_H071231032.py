k1 = input('\nMasukkan kata pertama: ').replace(' ','').lower()
k2 = input('Masukkan kata kedua: ').replace(' ','').lower()

x, y = 0, 0
for i in k1:
    x += k1.count(i)
    y += k2.count(i)
print(f'\nAnagram? {x == y}\n') if x == y else print(f'\nAnagram? {x == y}\n')