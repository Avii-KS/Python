s = input()
alphabets = 0
digits = 0
special_char = 0
for i in s:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
    else:
        special_char += 1
print(alphabets, digits, special_char)
