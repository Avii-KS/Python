class Solution:
    def numMovesStonesII(stones):
        stones.sort()  # Sort stones to arrange them on a number line

        n = len(stones)  # Number of stones

        # --- Max Moves ---
        # Move all outer stones inward by filling empty gaps one-by-one
        max_moves = max(
            stones[-1] - stones[1] - (n - 2),  # Leave first stone fixed
            stones[-2] - stones[0] - (n - 2)   # Leave last stone fixed
        )

        # --- Min Moves using Sliding Window ---
        min_moves = n  # Worst case: move all stones (will be reduced)
        left = 0       # Start of sliding window

        for right in range(n):  # Expand window using right pointer
            # Shrink window if the number of slots exceeds 'n'
            while stones[right] - stones[left] + 1 > n:
                left += 1  # Slide window to the right

            # Number of stones in current window
            window_size = right - left + 1

            # Special case: [1,2,3,4,6] → window has n−1 stones but still needs 2 moves
            if window_size == n - 1 and stones[right] - stones[left] + 1 == n - 1:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - window_size)

        return [min_moves, max_moves]  # Return result as [min, max]
