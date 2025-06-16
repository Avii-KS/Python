class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0  # Edge case: empty input

        left, right = 0, len(height) - 1  # Two pointers from both ends
        left_max, right_max = 0, 0        # Track the highest bar seen so far on both sides
        water = 0                         # Total water trapped

        while left < right:
            if height[left] < height[right]:
                # If left bar is smaller, process from the left side
                if height[left] >= left_max:
                    left_max = height[left]  # Update new left max
                else:
                    # Water trapped = difference between max and current height
                    water += left_max - height[left]
                left += 1  # Move left pointer right
            else:
                # If right bar is smaller, process from the right side
                if height[right] >= right_max:
                    right_max = height[right]  # Update right max
                else:
                    water += right_max - height[right]
                right -= 1  # Move right pointer left

        return water  # Total units of water trapped
