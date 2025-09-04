def maksimum(*x):
    maks = 0
    for i in x:
        for j in i:
            if j >= maks:
                maks = j
    return f'\nMaksimum = {maks}\n'
# try:
#     total = input('\nMasukkan angka: ')
#     total = [int(x) for x in total.split(' ')]
# except ValueError:
#     print("\nMasukan harus berupa angka.\n")
#     quit()
total = []
while True:
    try:
        x = input("\nMasukkan angka: ").lower()
        if x == 'done':
            break
        total.append(int(x))
    except ValueError:
        print("\nMasukan harus berupa angka.\n")
        quit()
print(maksimum(total))