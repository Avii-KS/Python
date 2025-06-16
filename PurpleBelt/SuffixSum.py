def suffixSum(arr):
    r=sum(arr)
    ss=[]
    for i in range(len(arr)):
        s= r-sum(arr[:i])
        ss.append(s)
    return ss
        
n=int(input())
arr=list(map(int,input().split()))
print(*suffixSum(arr))
