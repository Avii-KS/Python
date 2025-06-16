class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0  # To store the total number of valid arrangements
        used = [False] * (n + 1)  # To track which numbers are already placed

        # Backtracking function to try placing numbers at current index
        def backtrack(pos):
            # If we've placed all positions from 1 to n
            if pos > n:
                self.count += 1  # Found a valid arrangement
                return

            # Try placing every number from 1 to n
            for num in range(1, n + 1):
                # Only place if it hasn't been used and is beautiful at this position
                if not used[num] and (num % pos == 0 or pos % num == 0):
                    used[num] = True         # Mark number as used
                    backtrack(pos + 1)       # Recurse for the next position
                    used[num] = False        # Backtrack: unmark the number

        backtrack(1)  # Start placing numbers from position 1
        return self.count  # Return total beautiful arrangements
