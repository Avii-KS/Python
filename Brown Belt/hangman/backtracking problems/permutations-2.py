#same as basic permutations but now nums can contain duplicates

def backtracking(nums, path, used, result):
    #base case
    if len(path) == len(nums):
        if path not in result:
            result.append(path[:])
            return

    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            path.append(nums[i])
            backtracking(nums, path, used, result)
            path.pop()
            used[i] = False

def permute(nums):
    result = []
    used = [False]*len(nums)
    backtracking(nums, [], used, result)
    return result

nums = [1, 1, 2]
print(permute(nums))