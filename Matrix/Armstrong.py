n=input()
l=len(n)
s=0
for i in range(l):
  s+=int(n[i])**l
if s==int(n):
  print("Armstrong")
else:
  print("Not Armstrong")