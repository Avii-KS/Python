n=int(input())
s=list(map(int,input().split()))
if n not in s:
  print(-1)
else:
  for i in range(len(s)):
    if s[i]==n:
      print(i, end=" ")