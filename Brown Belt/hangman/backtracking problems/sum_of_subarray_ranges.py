def sum_of_subarray_ranges(n, nums):
    MOD = 10 ** 9 + 7

    def sum_subarray_contributions(is_max=True):
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        stack = []

        for i in range(n):
            while stack and ((nums[stack[-1]] > nums[i]) if is_max else (nums[stack[-1]] < nums[i])):
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and ((nums[stack[-1]] >= nums[i]) if is_max else (nums[stack[-1]] <= nums[i])):
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        total = 0
        for i in range(n):
            left_count = i - prev_smaller[i]
            right_count = next_smaller[i] - i
            total = (total + nums[i] * left_count * right_count)

        return total

    # Compute max contribution - min contribution
    return (sum_subarray_contributions(is_max=True) - sum_subarray_contributions(is_max=False))


# Example Usage:
n = 3
nums = [1, 2, 3]
print(-1*sum_of_subarray_ranges(n, nums))  # Output: 4