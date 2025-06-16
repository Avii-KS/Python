class Solution:
    def maximizeGreatness(self, nums):
        nums.sort()  # Step 1: Sort the array in ascending order

        i = 0  # Pointer to current element (original)
        j = 0  # Pointer to find strictly greater match
        n = len(nums)
        count = 0  # Greatness count

        # Step 2: Use two pointers to match each nums[i] to a greater nums[j]
        while j < n:
            if nums[i] < nums[j]:
                # Valid match found (nums[j] > nums[i])
                count += 1
                i += 1  # Move to next original number
            # Always move j to find next potential match
            j += 1

        return count  # Total greatness achieved
