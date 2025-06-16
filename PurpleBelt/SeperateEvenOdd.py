def SeperateEandO(arr):
    r1 = []
    r2 = []
    for i in arr:
        if i % 2 == 0:
            r1.append(i)
        else:
            r2.append(i)
    return r1, r2
    
n=int(input())
arr=list(map(int,input().split()))
even,odd= SeperateEandO(arr)
print(*even)
print(*odd)
