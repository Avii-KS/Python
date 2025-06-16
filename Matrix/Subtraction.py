m,n=map(int,input().split())
mat=[]
mat2=[]
for i in range(m):
    mat.append(list(map(int,input().split())))
for i in range(m):
    mat2.append(list(map(int,input().split())))

result = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        result[i][j] = mat[i][j] - mat2[i][j]

print("Matrix subtraction result:")

for i in result:
    print(' '.join(map(str, i)))