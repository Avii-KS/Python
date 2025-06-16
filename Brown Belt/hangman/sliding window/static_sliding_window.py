#static sliding window code to find the largest sum of k numbers
arr = [1, 2, 3, 4, 5, 6]
k = 3
curr_sum = 0
for i in range(k):
    curr_sum+=arr[i]
result = [curr_sum]

for i in range(1, len(arr)-k+1):
    curr_sum -= arr[i-1]
    curr_sum += arr[i+k-1]
    result.append(curr_sum)
print(result)
# improves time complexity from O(N*K) to O(N)