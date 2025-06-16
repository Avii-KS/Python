arr=list(map(int,input().split()))
prime_count=0
for i in arr:
  if i>1:
    is_prime=True
    for j in range(2,int(i**0.5)+1):
      if (i%j)==0:
        is_prime=False
        break
    else:
      prime_count+=1
print(prime_count)

  
