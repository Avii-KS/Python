def backtrack(nums, path, used, result):
    #base case
    if len(path) == len(nums):
        result.append(path[:])
        return

    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            path.append(nums[i])
            backtrack(nums, path, used, result)
            path.pop()
            used[i] = False

def permute(nums):
    result = []
    used = [False]*len(nums)
    backtrack(nums, [], used, result)
    return result
nums = [1, 2, 3]
print(permute(nums))