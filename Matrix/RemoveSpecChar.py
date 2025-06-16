def isalpha(s):
  for i in s:
    isalpha=False
    if i.isalpha():
      isalpha=True
      print(i,end="")
  return

s=input()
isalpha(s)