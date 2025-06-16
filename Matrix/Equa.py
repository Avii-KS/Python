m,n=map(int,input().split())
mat=[]
mat2=[]
for i in range(m):
    mat.append(list(map(int,input().split())))
for i in range(m):
    mat2.append(list(map(int,input().split())))
if (mat==mat2):
    print("Equal")
else:
    print("Not Equal")
    