def greaterandlower(arr):
    g=[]
    l=[]
    for i in arr:
        if i>m:
            g.append(i)
        else:
            l.append(i)
    print(*g)
    print(*l)
    
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
greaterandlower(arr)

