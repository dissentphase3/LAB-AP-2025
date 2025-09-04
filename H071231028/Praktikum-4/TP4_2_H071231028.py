
def palindrom(word: str) -> str:
    word = word.lower().replace(" ","")
    if word == word[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
print(palindrom(input("Masukkan kata atau frase: ")))