r1,c1=list(map(int,input().split()))
mat1=[]
for i in range(r1):
  mat1.append(list(map(int,input().split())))
mat2=[]
r2,c2=list(map(int,input().split()))
for i in range(r2):
  mat2.append(list(map(int,input().split())))
result=[[0 for j in range(c2)]for i in range(r1)]

for i in range(r1):
  for j in range(c2):
    for k in range(c1):
      result[i][j]+=mat1[i][k]*mat2[k][j]

for i in result:
  print(" ".join(map(str,i)))

s=0
for i in result:
  s+=sum(i)
print(s)

