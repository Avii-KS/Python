def SecondLargestEle(arr):
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr[1]


n=int(input())
arr=list(map(int,input().split()))
print(SecondLargestEle(arr))
