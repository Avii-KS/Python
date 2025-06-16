class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Helper function to calculate the max length of a window that can be turned into all 'target'
        # by flipping at most k characters (opposite of target)
        def maxLengthWithChar(target):
            left = 0           # Left pointer of the sliding window
            flips = 0          # Number of characters we have flipped in the current window
            max_len = 0        # Keep track of the longest valid window found so far

            # Iterate through the answerKey using right pointer
            for right in range(len(answerKey)):
                # If the current character is NOT the target (i.e., we would need to flip it)
                if answerKey[right] != target:
                    flips += 1  # We simulate flipping this character

                # If we have flipped more than k characters, shrink the window from the left
                while flips > k:
                    # If the character at 'left' was flipped before, we undo that flip
                    if answerKey[left] != target:
                        flips -= 1
                    left += 1  # Move the left boundary of the window to the right

                # Calculate current window length and update max_len if it's larger
                max_len = max(max_len, right - left + 1)

            # Return the length of the longest valid window with at most k flips to 'target'
            return max_len

        # Try both scenarios:
        # 1. Make as many 'T' as possible by flipping some 'F'
        # 2. Make as many 'F' as possible by flipping some 'T'
        # The answer is the max of the two
        return max(maxLengthWithChar('T'), maxLengthWithChar('F'))
