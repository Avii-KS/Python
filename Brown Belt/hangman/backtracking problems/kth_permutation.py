def backtracking(nums, path, used, result):
    if len(path) == len(nums):
        result.append(path[:])
        return

    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            path.append(nums[i])
            backtracking(nums, path, used, result)
            path.pop()
            used[i] = False

def permute(nums, k):
    result = []
    used = [False]*len(nums)
    backtracking(nums, [], used, result)
    return result[k-1]

n,k = map(int, input().split())
nums = [1, 2, 3]
for i in range(1, n+1):
    nums.append(i)
print(permute(nums, k))