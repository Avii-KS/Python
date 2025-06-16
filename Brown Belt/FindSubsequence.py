from itertools import combinations

def findSubsequences(nums):
    subsequences = set()
    
    for length in range(2, len(nums) + 1):
        for sub in combinations(nums, length):
            if list(sub) == sorted(sub):
                subsequences.add(sub)

    return sorted(subsequences)

# Taking input from the user
n = int(input())
nums = list(map(int, input().split()))

# Printing the result
for seq in findSubsequences(nums):
    print(*seq)