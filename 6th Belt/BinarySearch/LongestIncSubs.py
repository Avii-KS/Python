class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0  # Edge case: empty array

        n = len(nums)
        dp = [1] * n  # dp[i] = length of LIS ending at index i (each element is a LIS of at least 1)

        # Loop through the array to build the dp table
        for i in range(1, n):
            for j in range(i):
                # If nums[j] < nums[i], we can append nums[i] to an increasing subsequence ending at j
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)  # Take max between current dp[i] and dp[j]+1

        return max(dp)  # The maximum value in dp is the length of the LIS
