def duplicate(arr):
    elem=[]
    for i in arr:
        if i not in elem:
            elem.append(i)
    return elem
    
n=int(input())
arr=list(map(int,input().split()))
print(*duplicate(arr))