def sortedArray(arr1,arr2):
    r=arr1+arr2
    for i in range(len(r)):
        for j in range(len(r)-i-1):
            if r[j]>r[j+1]:
                r[j],r[j+1]=r[j+1],r[j]
    return r
        
n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
print(*sortedArray(arr1,arr2))
