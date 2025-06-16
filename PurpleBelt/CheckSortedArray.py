def Sorted(arr):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return 0
    return 1
    
n=int(input())
arr=list(map(int,input().split()))
print(Sorted(arr))
