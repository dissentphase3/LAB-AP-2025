def palindrom(kata: str) -> str:
    kata = kata.replace(" ", "").lower()
    if kata == kata[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
print(palindrom(input("masukkan kata ")))