class Solution:
    def findSubsequences(self, nums):
        res = []  # ✅ This will hold all valid subsequences we find

        # 🔁 Backtracking function to explore all paths
        def backtrack(start, path):
            # ✅ If the current path is long enough (≥ 2), save it
            if len(path) >= 2:
                res.append(path[:])  # Make a copy before adding

            used = set()  # 🔒 To prevent using the same number more than once at this level

            # 🔁 Try all numbers starting from 'start' index
            for i in range(start, len(nums)):

                # 🚫 If adding nums[i] breaks increasing order, skip it
                if path and nums[i] < path[-1]:
                    continue

                # 🚫 If nums[i] is already used at this level, skip to avoid duplicates
                if nums[i] in used:
                    continue

                used.add(nums[i])     # ✅ Mark this number as used at this recursion depth
                path.append(nums[i])  # ✅ Include this number in the current path
                backtrack(i + 1, path)  # 🔁 Explore next options starting from next index
                path.pop()            # 🔁 Undo the choice (backtrack)

        # 🚀 Start backtracking from index 0 with empty path
        backtrack(0, [])

        return res  # 🎯 Return all collected valid subsequences
