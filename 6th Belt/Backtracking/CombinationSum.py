class Solution:
    def combinationSum(self, candidates, target: int) :
        res = []  # This will store all valid combinations
        
        def backtrack(start, path, total):
            # ✅ Base Case: If total equals target, we've found a valid combination
            if total == target:
                res.append(path[:])  # Make a copy and store the result
                return
            # ❌ If total exceeds target, this path is invalid
            if total > target:
                return
            
            # Try each candidate starting from 'start' to avoid duplicates
            for i in range(start, len(candidates)):
                # Include candidates[i] in the current path
                path.append(candidates[i])
                # Recurse: stay at i (because we can reuse the same number)
                backtrack(i, path, total + candidates[i])
                # Backtrack: remove the last number to try another possibility
                path.pop()
        
        # Start backtracking with empty path and 0 total
        backtrack(0, [], 0)
        return res
