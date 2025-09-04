def catAndMouse(A,B,C):
    if (C-A)**2 < (C-B)**2:
        print("\nCat A\n")
    elif (C-A)**2 > (C-B)**2:
        print("\nCat B\n")
    else:
        print("\nMouse C\n")
A = int(input('\nA = '))
B = int(input('B = '))
C = int(input('C = '))
catAndMouse(A,B,C)