n=int(input())
mat=[]
# mat2=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
# for i in range(m):
#     mat2.append(list(map(int,input().split())))
result = [[0 for j in range(n)]for i in range (n)]
for i in range(n):
    for j in range(n):
        if i>=j:
            result[i][j]=mat[i][j]

for i in result:
    print(' '.join(map(str, i)))