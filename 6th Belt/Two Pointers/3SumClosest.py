class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()  # Step 1: Sort the array for two-pointer strategy
        n = len(nums)

        closest = float('inf')  # Initialize the closest sum (large placeholder)
        #closest stores the best (closest) sum we’ve found so far.We initialize it to infinity so any real sum will be closer.
        # Step 2: Iterate through each number as a potential first element of triplet
        for i in range(n - 2):  # We need at least 3 numbers,stopping at n-2 because we need three numbers for a triplet,Ensures there's always room for 2 more numbers
            left = i + 1        # Start the second pointer just after i
            right = n - 1       # Start the third pointer at the end

            # Step 3: Move two pointers towards each other
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If current_sum is closer to target than the previous closest, update it
                if abs(current_sum - target) < abs(closest - target): #We use abs(...) to compare distances.
                    closest = current_sum

                # If the current_sum is exactly the target, it's the closest possible
                if current_sum == target:
                    return target
                elif current_sum < target:
                    left += 1  # Need a bigger sum → move left to a bigger number
                else:
                    right -= 1  # Need a smaller sum → move right to a smaller number

        return closest  # Return the best sum found
    
#     This is the core of two-pointer logic:

# If the sum is too small, move left forward to increase it.

# If the sum is too big, move right backward to decrease it.

# This works because the array is sorted!

# for i in range(5 - 2) → for i in range(3) → i = 0, 1, 2
# Iterations:
# i = 0 → nums[0] = 1
# Use left = 1, right = 4 → check [1, 2, 5], [1, 3, 5]...

# i = 1 → nums[1] = 2
# Use left = 2, right = 4 → check [2, 3, 5], etc.

# i = 2 → nums[2] = 3
# Use left = 3, right = 4 → only one triplet left to try: [3, 4, 5]

# If we went to i = 3, then:

# left = 4, right = 4 → Only 1 element → ❌ Invalid triplet




