s=input()
r=""
for i in range(len(s)):
  r+=s[i]

  if i<len(s)-1 and s[i].islower() and s[i+1].isupper():
    r+=" "

print(r)
