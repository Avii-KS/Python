def longestOnes(nums, k):
    left = 0          # Left pointer of the sliding window
    zeros = 0         # Count of zeros in the current window
    max_len = 0       # To track the maximum length found

    for right in range(len(nums)):   # Right pointer expands the window
        if nums[right] == 0:
            zeros += 1              # Count zero in current window

        while zeros > k:            # If we’ve flipped more than k zeros, shrink the window
            if nums[left] == 0:
                zeros -= 1          # Remove a zero from the count if we're moving past it
            left += 1               # Shrink window from the left

        max_len = max(max_len, right - left + 1)  # Update max window size

    return max_len   # Return the largest window found
