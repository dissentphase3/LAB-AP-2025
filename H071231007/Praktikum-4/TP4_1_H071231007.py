def permutasi_kata(kata):
    try:
        n = int(kata)
        print('input harus berupa string')
    except :
        for i in range(len(kata)):
            kata = kata[-1] + kata[:-1]
            print(kata, end=' | ')

permutasi_kata(input())

