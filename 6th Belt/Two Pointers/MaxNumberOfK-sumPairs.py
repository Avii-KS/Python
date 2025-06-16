class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums.sort()  # Sort the array to apply two pointers
        left, right = 0, len(nums) - 1  # Two pointers at both ends
        count = 0  # Count of valid pairs

        while left < right:
            total = nums[left] + nums[right]  # Current sum of the pair

            if total == k:
                # Found a valid pair
                count += 1
                left += 1
                right -= 1  # Move both pointers inward
            elif total < k:
                # Too small, move left to try a bigger number
                left += 1
            else:
                # Too large, move right to try a smaller number
                right -= 1

        return count
