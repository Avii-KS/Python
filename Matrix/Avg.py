m,n=map(int,input().split())
mat=[]
# mat2=[]
for i in range(m):
    mat.append(list(map(int,input().split())))
# for i in range(m):
#     mat2.append(list(map(int,input().split())))

sum1 = 0

for i in range(m):
    for j in range(n):
        sum1 += mat[i][j]
avg = sum1/(m*n)
print(f"{avg:.1f}")