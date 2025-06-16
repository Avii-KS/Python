def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n  # Initialize DP array, each element starts with length 1

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:  # Check increasing condition
                dp[i] = max(dp[i], dp[j] + 1)  # Update maximum subsequence length

    return max(dp)  # Return the longest increasing subsequence length

# Taking input from the user
n = int(input())
nums = list(map(int, input().split()))

print(lengthOfLIS(nums))