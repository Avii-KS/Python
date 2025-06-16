m,n=3,3
mat=[]
mat2=[]
for i in range(m):
    mat.append(list(map(int,input().split())))
for i in range(m):
    mat2.append(list(map(int,input().split())))

result = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        for k in range(m):
            result[i][j] += mat[i][k] * mat2[k][j]

for i in result:
    print(' '.join(map(str, i)))
