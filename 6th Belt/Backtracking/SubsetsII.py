class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # ✅ Sort to bring duplicates together
        res = []     # Stores all unique subsets

        def backtrack(start, path):
            res.append(path[:])  # Always add the current subset

            for i in range(start, len(nums)):
                # ❌ Skip duplicates at the same recursive depth
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])           # Choose nums[i]
                backtrack(i + 1, path)        # Explore further
                path.pop()                    # Backtrack and undo

        backtrack(0, [])  # Start recursion
        return res
