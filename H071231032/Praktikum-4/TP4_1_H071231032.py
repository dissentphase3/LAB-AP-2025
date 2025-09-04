def stringPermutation(kata):
    try:
        float(kata) or int(kata)
        raise TypeError("\nInputan harus string.\n")
    except TypeError as error:
        print(error)
    except ValueError:
        if len(kata) == 0:
            print("\nInputan tidak boleh kosong.\n")
            quit()
        deretPermutasi = ''
        for _ in range(len(kata)):
            kata = kata[len(kata)-1]+ kata[:len(kata)-1]
            deretPermutasi += kata + ' | '
        print('\n' + deretPermutasi + '\n')
stringPermutation(input("\nMasukkan kata: ").replace(' ',''))