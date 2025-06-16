#Recursive Backtracking

#Solution to find all possible subsets of an array on numbers using recursive backtracking

nums = [1, 2, 3]
def subsets(nums):
    n = len(nums)
    res, sol = [], []

    def backtrack(i):
        #base case
        if i == n:
            res.append(sol[:])
            return

        #Dont pick nums[i]
        backtrack(i+1)

        #Pick nums[i]
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)
    return res

print(subsets(nums))