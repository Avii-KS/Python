#using two pointer approach

def trap_rainwater(n, heights):
    if n == 0:
        return 0
    trapped_water = 0
    left, right = 0, n-1
    left_max, right_max = heights[left], heights[right]
    while left<right:
        if left_max<right_max:
            left+=1
            if left_max<heights[left]:
                left_max = heights[left]
            if left_max-heights[left]>0:
                trapped_water += left_max-heights[left]
        else:
            right-=1
            if right_max<heights[right]:
                right_max = heights[right]
            if right_max-heights[right]>0:
                trapped_water+=right_max-heights[right]
    return trapped_water

# Example Usage:
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(heights)
print(trap_rainwater(n, heights))  # Output: 6
