m=int(input())
n=list(map(int,input().split()))
sum=0
avg=0
for i in n:
  sum=sum+i
avg=sum/m
print(avg)
print(sum)
