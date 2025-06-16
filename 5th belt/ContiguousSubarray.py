def find_subarray_with_sum(arr, k):
    prefix_sum = {}
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == k:
            return (0, i)
        if current_sum - k in prefix_sum:
            return (prefix_sum[current_sum - k] + 1, i)
        prefix_sum[current_sum] = i

    return "No subarray found"

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
result = find_subarray_with_sum(arr, k)

if isinstance(result, tuple):
    print(result[0], result[1])
else:
    print(result)