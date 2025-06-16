n = int(input())
if n == 0:
    print(0)
else:
    arr = list(map(int, input().split()))
    prefixSum = [0 for i in range(n)]
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]
    for i in range(n):
        print(prefixSum[i], end=" ")
