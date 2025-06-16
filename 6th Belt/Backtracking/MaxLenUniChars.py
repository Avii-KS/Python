class Solution:
    def maxLength(self, arr) -> int:
        res = 0  # 🔹 This keeps track of the longest valid string we’ve built so far

        # 🔧 A helper function using backtracking
        def backtrack(index, current):
            nonlocal res  # So we can update the outer res variable inside this function(It allows the inner function to modify a variable defined in the outer function.)

            # 🚫 If the current string has duplicate letters, stop exploring this path
            if len(current) != len(set(current)):
                return

            # ✅ If it's valid (no duplicates), update max result
            res = max(res, len(current))

            # 🔁 Try to add the next string (from index to end of list)
            for i in range(index, len(arr)):
                # 🔀 Try including arr[i] in current and recurse forward  
                backtrack(i + 1, current + arr[i])

        # 🚀 Start the backtracking process from the beginning
        backtrack(0, "")
        return res  # 🎯 Final answer: longest unique-character string length
    

#     i in range(index, ...)	Start from current position and try all remaining strings
# backtrack(i + 1, ...)	Move forward, skip already used strings, and avoid duplicates
# Why i + 1?	Because we want combinations (not permutations), and no repeated elements
# What if we use i?	We’d allow reusing the same string again → not correct for this problem
