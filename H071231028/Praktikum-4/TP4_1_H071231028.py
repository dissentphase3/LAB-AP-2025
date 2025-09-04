def string_permutation(word):
    deret = ""
    if len(word) <= 1:
        print(word)
    else:
        for _ in range(len(word)):
            word = word[-1] + word[:-1]
            deret += word + ' | '
    print(deret)

string_permutation(input('Masukkan kata: '))
                    






