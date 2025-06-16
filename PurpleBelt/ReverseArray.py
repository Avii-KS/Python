def ReverseArr(arr):
    arr=arr[::-1]
    return arr
    
n=int(input())
arr=list(map(int,input().split()))
print(*ReverseArr(arr))