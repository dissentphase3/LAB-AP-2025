while True:
    try:
        x = [int(i) for i in input('\nMasukkan beberapa angka (pisahkan dengan spasi):\033[93m ').split(' ')]
        angkaGanjil, angkaGenap, kelipatanLima = set(), set(), set()
        for i in x:
            if i % 2 == 0:
                angkaGenap.add(i)
            if i % 2 != 0:
                angkaGanjil.add(i)
            if i % 5 == 0:
                kelipatanLima.add(i)
        print(f"\n\033[0mAngka genap: \033[93m{sorted(list(angkaGenap))}\033[0m\nAngka ganjil: \033[93m{sorted(list(angkaGanjil))}\033[0m\nAngka yang habis dibagi lima: \033[93m{sorted(list(kelipatanLima))}\n")
        break
    except ValueError:
        print('\n\033[35mInputan invalid.\033[0m')