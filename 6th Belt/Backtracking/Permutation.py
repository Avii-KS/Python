class Solution:
    def permute(self, nums) :
        res = []  # Stores all permutations

        def backtrack(path, used):
            if len(path) == len(nums):  # ✅ If path contains all numbers, it's a valid permutation
                res.append(path[:])     # Add a copy of the current path to the result
                return

            for i in range(len(nums)):
                if used[i]:             # ❌ Skip if the number is already used in current path
                    continue
                used[i] = True          # ✅ Mark this number as used
                path.append(nums[i])   # Add the number to current permutation path
                backtrack(path, used)  # Recurse to build the rest of the permutation
                path.pop()             # 🔙 Backtrack: remove the number from path
                used[i] = False        # ✅ Mark the number as unused again

        backtrack([], [False] * len(nums))  # Start with empty path and unused flags
        return res
