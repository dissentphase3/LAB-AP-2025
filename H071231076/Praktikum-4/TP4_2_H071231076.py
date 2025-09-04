def is_palindrome(word: str) -> str:
    panjang_kata = word.lower().replace(" ", "")
    rotated_word = panjang_kata[::-1] #Membalikkan kata
    if panjang_kata == rotated_word:
        return 'palindrom'
    else :
        return 'Bukan palindrom'

kata = input()
print(f'palindrom("{kata}")')
print(is_palindrome(kata))