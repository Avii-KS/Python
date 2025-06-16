n=int(input())
r=0
for i in range(len(str(n))):
  r+=int(str(n)[i])**len(str(n))
if r==n:
  print("True")
else:
  print("False")