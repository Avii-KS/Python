def reduced_form(n,d):
  for i in range(2,d+1):
    if n%i==0 and d%i==0:
      return[n//i,d//i]
      break
  return n,d

n,d=map(int,input().split())
reduced=reduced_form(n,d)
print(f"{reduced[0]}/{reduced[1]}")