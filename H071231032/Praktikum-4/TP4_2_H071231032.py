def palindrom(x: str) -> str:
    x = x.replace(' ','').lower()
    print('\n'+x)
    print(x[::-1])
    if x == x[::-1]:
        return "\nPalindrom\n"
    else:
        return "\nBukan Palindrom\n"
print(palindrom(input("Masukkan kata: ")))