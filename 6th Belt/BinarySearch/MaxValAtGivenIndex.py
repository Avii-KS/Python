class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # Helper function to calculate total sum required if we set nums[index] = x
        def calc(x):
            left_len = index  # Number of elements to the left of the index
            right_len = n - index - 1  # Number of elements to the right

            # Calculate left sum: form decreasing sequence of length 'left_len' starting from x-1
            if x > left_len:
                # Full pyramid fits on the left, so arithmetic sum: (first + last) * count / 2
                left_sum = (x - 1 + x - left_len) * left_len // 2
            else:
                # Pyramid hits floor (1) before filling left side, so fill (x-1 to 1), rest are 1s
                left_sum = (x - 1) * x // 2 + (left_len - (x - 1))

            # Calculate right sum similarly for right side
            if x > right_len:
                right_sum = (x - 1 + x - right_len) * right_len // 2
            else:
                right_sum = (x - 1) * x // 2 + (right_len - (x - 1))

            # Total sum = left side + right side + center element (x)
            return left_sum + right_sum + x

        # Binary search for the maximum possible value at index such that total sum ≤ maxSum
        low, high = 1, maxSum  # Lower and upper bounds for x (must be at least 1)

        while low < high:
            mid = (low + high + 1) // 2  # Try the middle value as a candidate x

            if calc(mid) <= maxSum:
                low = mid  # mid is a valid value, try to go higher
            else:
                high = mid - 1  # mid causes sum to exceed maxS
