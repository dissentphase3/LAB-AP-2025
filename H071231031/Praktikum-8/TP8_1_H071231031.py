import re
pattern = r'^[a-zA-Z24680]{40}[13579\s]{5}$'
user_input = input()
print(True) if re.match(pattern, user_input) else print(False)