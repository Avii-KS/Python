def totalFruit(fruits):
    from collections import defaultdict

    count = defaultdict(int)  # Dictionary to keep track of fruit types in the current window
    left = 0                  # Left pointer of the sliding window
    max_len = 0               # To store the maximum number of fruits we can collect

    for right in range(len(fruits)):  # Iterate over each tree using the right pointer
        count[fruits[right]] += 1     # Add the current fruit type to our basket (increase count)

        while len(count) > 2:         # If we have more than 2 types, shrink window from the left
            count[fruits[left]] -= 1  # Remove one fruit from the leftmost type
            if count[fruits[left]] == 0:  # If no more fruits of that type are left
                del count[fruits[left]]   # Remove that fruit type from the basket
            left += 1                # Move the left pointer forward to shrink the window

        max_len = max(max_len, right - left + 1)  # Update max length of valid window

    return max_len  # Return the largest number of fruits we could collect
