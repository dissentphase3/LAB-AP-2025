def kata(word: str) -> str:
    bacaan = word.lower().replace(' ', '')
    try:
        if bacaan == bacaan[::-1]:
            return "Palindrom"
        else:
            return "Bukan Palindrom"
    except TypeError:
        print("type error")

input_word = input("Masukkan sebuah kata: ")

hasil = kata(input_word)
print(f"'{input_word}' adalah {hasil}")
