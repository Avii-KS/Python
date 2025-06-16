class Solution:
    def letterCombinations(self, digits: str):
        # If input is empty, return empty list
        if not digits:
            return []

        # Mapping from digits to letters (like a phone keypad)
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = []  # To store all combinations

        # Backtracking function
        def backtrack(index, path):
            # Base case: If the path length == digits length, we have a full combination
            if index == len(digits):
                res.append("".join(path))  # Join characters and add to result
                return

            # Get the letters mapped to the current digit
            possible_letters = digit_to_char[digits[index]]

            # Try every letter for the current digit
            for char in possible_letters:
                path.append(char)           # Choose
                backtrack(index + 1, path)  # Explore
                path.pop()                  # Undo choice (backtrack)

        backtrack(0, [])  # Start from index 0 with empty path
        return res
