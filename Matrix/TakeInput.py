m,n = map(int,input().split())

mat = []
for i in range(m):
    mat.append(list(map(int,input().split())))
    

for i in mat:
    print(' '.join(map(str, i)))
