class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n  # Initialize all answers with -1 (default if no NGE found)
        stack = []  # This will store indices of nums (not values)

        # We simulate the circular array by looping twice (2n - 1 to 0)
        for i in range(2 * n - 1, -1, -1):
            index = i % n  # Wrap around the array using modulo, to simulate circular behavior.

            # ⚙️ Maintain decreasing stack: pop until you find a bigger element
            while stack and nums[stack[-1]] <= nums[index]:
                stack.pop() # Pop smaller elements; they can't be next greater for current

            # If we are in the first pass (i < n), we assign the result
            if i < n:
                if stack:
                    res[index] = nums[stack[-1]]  # Next greater is on top of the stack
                # else: res[index] stays -1 (default)

            stack.append(index)  # Push current index to stack

        return res

#We loop through the array twice, but each element is pushed/popped at most once from the stack.
#  Why Traverse 2n Times?
# To simulate the circular behavior:

# We imagine going through the array twice.

# That means we check 2 * n elements using i % n to simulate circular indexing.

# This way, every element gets a chance to look forward across the full circle.

# We use i % n to get the actual index in nums.

#  2. Intuition
# “Since the array is circular, every element may need to look not only ahead but also at the beginning of the array to find the next greater number.
# To efficiently find the next greater element for each index, we can use a monotonic decreasing stack and simulate the circular behavior by iterating through the array twice.”

# 🛠️ 3. Approach
# “Here’s how I solve it step-by-step:

# Initialize a result array res with -1 (default: no greater found).

# Use a stack to keep track of indices of elements for which we haven't found the NGE yet.

# Loop from 2n - 1 to 0 (simulate circular array).

# At each step i, use i % n to access the real index in nums.

# While the current number is greater than or equal to the element at the index on top of the stack, we pop from the stack (because we found a greater element).

# If the stack is not empty, it means the top of the stack has the next greater element for this index.

# Push the current index to the stack so it can be the NGE for earlier elements.

# This gives an efficient O(n) solution.”

# 🔄 4. Circular Handling
# “We simulate the circular nature by looping 2 * n times.
# The second loop helps us find NGEs for the elements at the end of the array that might find their NGE at the beginning (like 3 → 4 in [1,2,3,4,3]).”





  