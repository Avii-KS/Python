#find longest substring of 1s if k 0s are changed to 1s
def longestOnes(nums, k):
    left = 0
    max_ones=0
    zeros_flipped = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_flipped+=1
        while zeros_flipped>k:
            if nums[left]==0:
                zeros_flipped-=1
            left+=1

        max_ones = max(max_ones, right-left+1)
    return max_ones
nums=[0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
k=2
print(longestOnes(nums, k))