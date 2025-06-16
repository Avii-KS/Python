def sum_of_subarray_mins(n, arr):
    MOD = 10 ** 9 + 7

    # Stacks for finding previous and next smaller elements
    result = 0
    prev_smaller = [-1] * n
    next_smaller = [n] * n
    stack = []

    # Finding Previous Smaller Elements (PSE)
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()

    # Finding Next Smaller Elements (NSE)
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        next_smaller[i] = stack[-1] if stack else n
        stack.append(i)

    # Calculating sum of min(subarray) using contribution of each element
    for i in range(n):
        left_count = i - prev_smaller[i]
        right_count = next_smaller[i] - i
        result = (result + arr[i] * left_count * right_count) % MOD

    return result


# Example Usage:
arr = [3, 1, 2, 4]
n = len(arr)
print(sum_of_subarray_mins(n, arr))  # Output: 17
