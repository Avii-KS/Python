class Solution:
    def partition(self, s: str):
        res = []  # Store all valid palindrome partitions

        def is_palindrome(sub):
            return sub == sub[::-1]  # Check if substring is a palindrome

        def backtrack(start, path):
            if start == len(s):  # ✅ If we've reached the end, add current partition
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):  # Try all substrings starting from 'start'
                if is_palindrome(s[start:end]):  # ✅ Proceed only if the substring is a palindrome
                    path.append(s[start:end])   # Choose the palindrome substring
                    backtrack(end, path)        # Recurse for the rest of the string
                    path.pop()                  # 🔙 Backtrack: remove last added substring

        backtrack(0, [])  # Start from index 0 with empty path
        return res