def toggle(s):
    r=""
    for i in s:
        if i.isupper():
            r+=i.lower()
        else:
            r+=i.upper()
    return r
    
    
s=input()
print(toggle(s))
