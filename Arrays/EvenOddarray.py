# Use print() to print to the console
n=int(input())
a=list(map(int,input().split()))
isEven = True
for i in a:
  if (i%2==0):
    isEven = True
    break
  else:
    isEven = False
if isEven:
  print("E")
else:
  print("O")