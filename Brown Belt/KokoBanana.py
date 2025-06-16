import math

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        hours = sum(math.ceil(pile / mid) for pile in piles)

        if hours > h:
            left = mid + 1
        else:
            right = mid

    return left

# Taking input from the user
n = int(input())  # Number of piles
piles = list(map(int, input().split()))  # Banana piles
h = int(input())  # Hours available

print(minEatingSpeed(piles, h))