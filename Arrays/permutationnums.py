n=int(input())
nums=list(map(int,input().split()))
r=[]
ans=0
for i in range(n):
  ans=nums[nums[i]]
  r.append(ans)
print(*r)

