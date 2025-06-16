def maxValue(n, index, maxSum):
    left, right = 1, maxSum

    def sum_of_ap(n, max_element):
        if max_element >= n:
            return (max_element * (max_element + 1)) // 2 - ((max_element - n) * (max_element - n + 1)) // 2
        else:
            return (max_element * (max_element + 1)) // 2 + (n - max_element)

    while left < right:
        mid = (left + right + 1) // 2
        left_sum = sum_of_ap(index + 1, mid)
        right_sum = sum_of_ap(n - index, mid)
        
        if left_sum + right_sum - mid <= maxSum:
            left = mid
        else:
            right = mid - 1

    return left

# Taking input from the user
n = int(input())
index = int(input())
maxSum = int(input())

print(maxValue(n, index, maxSum))