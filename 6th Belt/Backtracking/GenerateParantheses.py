class Solution:
    def generateParenthesis(self, n: int) :
        res = []  # To store all valid combinations

        # Helper function to build the parentheses string
        def backtrack(current, open_count, close_count):
            # Base case: when the current string has 2n characters (n pairs)
            if len(current) == 2 * n:
                res.append(current)  # It's a valid combination, add to results
                return

            # If we can still add an open parenthesis (we haven’t used up all 'n')
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)  # Add '(' and move forward

            # If we can add a close parenthesis (must not exceed number of open ones)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)  # Add ')' and move forward

        # Start recursion with an empty string and zero open/close parentheses used
        backtrack("", 0, 0)

        return res  # Return all valid combinations
