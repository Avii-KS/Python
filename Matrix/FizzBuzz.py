n=int(input())
for i in range(1,n+1):
  if i%3==0:
    print("Fizz",end=" ")
  elif i%5==0:
    print("Buzz",end=" ")
  elif i%3==0 and i%5==0:
    print("FizzBuzz",end=" ")
  elif n>100:
    print("-1")
    break
  else:
    print(i,end=" ")