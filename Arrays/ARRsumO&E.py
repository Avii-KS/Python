n=int(input())
l=list(map(int,input().split()))
odd=0
even=0
for i in range(len(l)):
  if l[i]%2==0:
    even=even+l[i]
  else:
    odd=odd+l[i]
print(odd-even)