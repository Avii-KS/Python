class Solution:
    def numSubarrayBoundedMax( nums, left: int, right: int) -> int:
        # Helper to count subarrays where all elements are ≤ bound
        def count(bound):
            count = 0         # Count of valid subarrays
            current = 0       # Number of valid subarrays ending at current position

            for num in nums:
                if num <= bound:
                    current += 1     # Extend previous subarrays + 1 new subarray
                else:
                    current = 0      # Reset, as num > bound breaks the subarray

                count += current     # Add current count to total

            return count

        # Total valid = subarrays where max ≤ right - subarrays where max < left
        return count(right) - count(left - 1)
