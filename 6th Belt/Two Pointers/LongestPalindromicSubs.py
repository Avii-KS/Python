class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s  # Single character or empty string is itself a palindrome

        start, end = 0, 0  # To keep track of the longest palindrome boundaries

        # Helper function to expand around center and return valid palindrome bounds
        def expandFromCenter(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the bounds of the palindrome (not including right)
            return left + 1, right - 1

        for i in range(len(s)):
            # Case 1: Odd-length palindrome (center at i)
            l1, r1 = expandFromCenter(i, i)
            # Case 2: Even-length palindrome (center between i and i+1)
            l2, r2 = expandFromCenter(i, i + 1)

            # Choose the longer of the two
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        # Return the substring that is the longest palindrome
        return s[start:end + 1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]  # Check if string is same forwards and backwards

        longest = ""
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if isPalindrome(substring) and len(substring) > len(longest):
                    longest = substring  # Update if it's a longer palindrome

        return longest
