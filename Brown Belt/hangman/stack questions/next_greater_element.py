def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}

    # Iterate through nums2 and fill the next_greater map
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)
        print("stack", stack)
    # Map remaining elements to -1
    while stack:
        next_greater[stack.pop()] = -1
    print("dict", next_greater)
    # Build the result array using the next_greater map
    return [next_greater[num] for num in nums1]


# Example usage
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]
