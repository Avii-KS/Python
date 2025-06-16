def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return -1

n = int(input())
nums = list(map(int, input().split()))
target = int(input())
result = two_sum(nums, target)
if result == -1:
    print(result)
else:
    print(*result)