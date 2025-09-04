import re
string = input()
pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
result = re.match(pattern, string)
if result:
    print("True")
else :
    print("False")