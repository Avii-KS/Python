m,n=map(int,input().split())
mat=[]
mat2=[]
for i in range(m):
    mat.append(list(map(int,input().split())))
for i in range(m):
    mat2.append(list(map(int,input().split())))

result = [[0 for j in range(m)] for i in range(n)]

for i in range(m):
    for j in range(n):
        result[j][i] = mat[i][j]

for i in result:
    print(' '.join(map(str, i)))